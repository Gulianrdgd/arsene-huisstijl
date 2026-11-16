"""Build the Office templates in templates/ from the design tokens.

    python3 -m pip install python-docx python-pptx
    python3 scripts/build-office.py

Needs `rsvg-convert` (librsvg) to turn the logo SVGs into PNGs, because Word and
PowerPoint templates built this way embed raster images. Fonts are not embedded:
install Geist and Geist Mono from fonts/ first.

Output:
    templates/Arsene_document.dotx     rapport, offerte, notitie
    templates/Arsene_brief.dotx        brief
    templates/Arsene_presentatie.potx  presentatie 16:9, met voorbeelddia's
"""

import copy
import json
import re
import shutil
import subprocess
import tempfile
import zipfile
from pathlib import Path

from docx import Document
from docx.enum.section import WD_SECTION
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_BREAK, WD_TAB_ALIGNMENT
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn
from docx.shared import Mm, Pt, RGBColor
from lxml import etree
from pptx import Presentation
from pptx.enum.shapes import PP_PLACEHOLDER
from pptx.opc.constants import RELATIONSHIP_TYPE as RT
from pptx.oxml.ns import qn as pqn
from pptx.util import Emu, Inches
from pptx.util import Pt as PPt

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "templates"
TOKENS = json.loads((ROOT / "design-system/tokens.json").read_text())
C = {c["name"]: c["value"].lstrip("#").upper() for c in TOKENS["color"]["palette"]}
CHART = {t["name"]: t["light"] for t in TOKENS["color"]["chart"]["tokens"]}

SANS, SEMI, MEDIUM, MONO = "Geist", "Geist SemiBold", "Geist Medium", "Geist Mono"
A = "http://schemas.openxmlformats.org/drawingml/2006/main"


def hexval(name_or_hex):
    v = C.get(name_or_hex, name_or_hex)
    return v.lstrip("#").upper()


# ---------------------------------------------------------------- shared theme

def theme_xml(blob):
    """Brand colours and Geist in an Office theme part."""
    accents = [CHART["chart-1"], CHART["chart-2"], CHART["chart-3"], CHART["chart-4"], "warm-400", "warm-800"]
    accents = [hexval(a) for a in accents]
    clr = (
        f'<a:clrScheme xmlns:a="{A}" name="Arsene">'
        f'<a:dk1><a:srgbClr val="{C["ink"]}"/></a:dk1><a:lt1><a:srgbClr val="FFFFFF"/></a:lt1>'
        f'<a:dk2><a:srgbClr val="{C["teal-deep"]}"/></a:dk2><a:lt2><a:srgbClr val="{C["paper"]}"/></a:lt2>'
        + "".join(f'<a:accent{i}><a:srgbClr val="{v}"/></a:accent{i}>' for i, v in enumerate(accents, 1))
        + f'<a:hlink><a:srgbClr val="{C["mint-deep"]}"/></a:hlink><a:folHlink><a:srgbClr val="{C["warm-800"]}"/></a:folHlink>'
        "</a:clrScheme>"
    )
    font = (
        f'<a:fontScheme xmlns:a="{A}" name="Arsene">'
        f'<a:majorFont><a:latin typeface="{SANS}"/><a:ea typeface=""/><a:cs typeface=""/></a:majorFont>'
        f'<a:minorFont><a:latin typeface="{SANS}"/><a:ea typeface=""/><a:cs typeface=""/></a:minorFont>'
        "</a:fontScheme>"
    )
    root = etree.fromstring(blob)
    elements = root.find(f"{{{A}}}themeElements")
    for tag, xml in (("clrScheme", clr), ("fontScheme", font)):
        old = elements.find(f"{{{A}}}{tag}")
        elements.replace(old, etree.fromstring(xml))
    root.set("name", "Arsene")
    return etree.tostring(root, xml_declaration=True, encoding="UTF-8", standalone=True)


def as_template(src, dst, main_part, template_type):
    """Rewrite a .docx/.pptx into a .dotx/.potx by changing the main content type."""
    with zipfile.ZipFile(src) as zin, zipfile.ZipFile(dst, "w", zipfile.ZIP_DEFLATED) as zout:
        for item in zin.infolist():
            data = zin.read(item.filename)
            if item.filename == "[Content_Types].xml":
                data = re.sub(
                    rf'(PartName="{re.escape(main_part)}" ContentType=")[^"]+"'.encode(),
                    rf'\g<1>{template_type}"'.encode(),
                    data,
                )
            zout.writestr(item, data)


def logo_pngs(tmp):
    out = {}
    for name, height in (("arsene-wordmark-ink", 300), ("arsene-wordmark-paper", 300), ("arsene-icon", 512)):
        png = tmp / f"{name}.png"
        subprocess.run(["rsvg-convert", "-h", str(height), str(ROOT / f"assets/logo/{name}.svg"), "-o", str(png)], check=True)
        out[name] = png
    return out


# ---------------------------------------------------------------------- Word

def set_run_props(rpr_parent, font=None, size=None, color=None, bold=None, italic=None, caps=None, tracking_pt=None):
    """Set character properties on a style (python-docx style.font + raw XML for the rest)."""
    f = rpr_parent.font
    if font:
        f.name = font
        rfonts = rpr_parent.element.get_or_add_rPr().get_or_add_rFonts()
        for attr in ("w:ascii", "w:hAnsi", "w:cs", "w:eastAsia"):
            rfonts.set(qn(attr), font)
    if size:
        f.size = Pt(size)
    if color:
        f.color.rgb = RGBColor.from_string(hexval(color))
    if bold is not None:
        f.bold = bold
    if italic is not None:
        f.italic = italic
    if caps is not None:
        f.all_caps = caps
    if tracking_pt is not None:
        rpr = rpr_parent.element.get_or_add_rPr()
        spacing = rpr.find(qn("w:spacing"))
        if spacing is None:
            spacing = OxmlElement("w:spacing")
            rpr.append(spacing)
        spacing.set(qn("w:val"), str(round(tracking_pt * 20)))


def para_style(doc, name, base="Normal", **kw):
    styles = doc.styles
    try:
        st = styles[name]
    except KeyError:
        st = styles.add_style(name, 1)
        st.base_style = styles[base]
        st.quick_style = True
    pf = st.paragraph_format
    for key in ("space_before", "space_after"):
        if key in kw:
            setattr(pf, key, Pt(kw.pop(key)))
    if "line" in kw:
        pf.line_spacing = kw.pop("line")
    if "keep_next" in kw:
        pf.keep_with_next = kw.pop("keep_next")
    rule = kw.pop("rule_above", False)
    set_run_props(st, **kw)
    if rule:
        ppr = st.element.get_or_add_pPr()
        ppr.append(parse_xml(
            f'<w:pBdr {nsdecls("w")}><w:top w:val="single" w:sz="8" w:space="6" w:color="{C["ink"]}"/></w:pBdr>'))
    return st


def word_styles(doc):
    para_style(doc, "Normal", font=SANS, size=10, color="warm-800", space_after=6, line=1.3)
    para_style(doc, "Title", font=SANS, size=40, bold=True, color="ink", tracking_pt=-1.8, space_after=10, line=0.95)
    para_style(doc, "Intro", font=SANS, size=12, color="warm-800", space_after=14, line=1.35)
    para_style(doc, "Heading 1", font=SANS, size=26, bold=True, color="ink", tracking_pt=-0.9, space_before=24, space_after=8, line=1.0, keep_next=True)
    para_style(doc, "Heading 2", font=SEMI, size=13, bold=False, color="ink", tracking_pt=-0.13, space_before=18, space_after=6, line=1.15, keep_next=True, rule_above=True)
    para_style(doc, "Heading 3", font=SEMI, size=10, bold=False, color="ink", space_before=12, space_after=3, line=1.2, keep_next=True)
    para_style(doc, "Caption", font=SANS, size=8.5, bold=False, italic=False, color="warm-600", space_before=4, space_after=10, line=1.3)
    para_style(doc, "Lopende kop", font=MONO, size=8, color="warm-600", caps=True, tracking_pt=0.64, space_after=0, line=1.0)
    for name in ("List Bullet", "List Number"):
        para_style(doc, name, font=SANS, size=10, color="warm-800", space_after=3, line=1.3)
    # Plain headings: no theme colour or italic left over from the default template
    for name in ("Heading 1", "Heading 2", "Heading 3", "Title"):
        rpr = doc.styles[name].element.get_or_add_rPr()
        for tag in ("w:i", "w:iCs"):
            el = rpr.find(qn(tag))
            if el is not None:
                rpr.remove(el)
    title_ppr = doc.styles["Title"].element.get_or_add_pPr()
    for bdr in title_ppr.findall(qn("w:pBdr")):
        title_ppr.remove(bdr)

    doc.styles.element.append(parse_xml(
        f'<w:style {nsdecls("w")} w:type="table" w:customStyle="1" w:styleId="ArseneTabel">'
        '<w:name w:val="Arsene tabel"/><w:basedOn w:val="TableNormal"/><w:uiPriority w:val="40"/><w:qFormat/>'
        '<w:pPr><w:spacing w:before="60" w:after="60" w:line="240" w:lineRule="auto"/></w:pPr>'
        f'<w:rPr><w:rFonts w:ascii="{SANS}" w:hAnsi="{SANS}" w:cs="{SANS}"/><w:color w:val="{C["ink"]}"/><w:sz w:val="18"/></w:rPr>'
        '<w:tblPr><w:tblBorders>'
        f'<w:bottom w:val="single" w:sz="4" w:space="0" w:color="{C["warm-400"]}"/>'
        f'<w:insideH w:val="single" w:sz="4" w:space="0" w:color="{C["warm-400"]}"/>'
        '</w:tblBorders><w:tblCellMar><w:top w:w="40" w:type="dxa"/><w:left w:w="0" w:type="dxa"/>'
        '<w:bottom w:w="40" w:type="dxa"/><w:right w:w="170" w:type="dxa"/></w:tblCellMar></w:tblPr>'
        '<w:tblStylePr w:type="firstRow"><w:rPr>'
        f'<w:rFonts w:ascii="{SEMI}" w:hAnsi="{SEMI}" w:cs="{SEMI}"/></w:rPr>'
        f'<w:tcPr><w:tcBorders><w:bottom w:val="single" w:sz="8" w:space="0" w:color="{C["ink"]}"/></w:tcBorders></w:tcPr>'
        '</w:tblStylePr></w:style>'))


def field(paragraph, instr, style_run=None):
    run = paragraph.add_run()
    fld = OxmlElement("w:fldSimple")
    fld.set(qn("w:instr"), instr)
    r = OxmlElement("w:r")
    t = OxmlElement("w:t")
    t.text = "00"
    r.append(t)
    fld.append(r)
    run._r.addnext(fld)
    return fld


def page_setup(section, top=22):
    section.page_width, section.page_height = Mm(210), Mm(297)
    section.left_margin = section.right_margin = Mm(18)
    section.top_margin, section.bottom_margin = Mm(top), Mm(20)
    section.header_distance = section.footer_distance = Mm(10)


def header_footer(section, logos, running_field=True):
    text_width = Mm(210 - 36)
    hp = section.header.paragraphs[0]
    hp.style = "Lopende kop"
    hp.paragraph_format.tab_stops.add_tab_stop(text_width, WD_TAB_ALIGNMENT.RIGHT)
    hp.add_run().add_picture(str(logos["arsene-wordmark-ink"]), height=Mm(4.2))
    hp.add_run("\t")
    if running_field:
        field(hp, ' STYLEREF "Heading 1" \\* MERGEFORMAT ')
    fp = section.footer.paragraphs[0]
    fp.style = "Lopende kop"
    fp.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    field(fp, ' PAGE \\# "00" ')
    fp.add_run(" / ")
    field(fp, ' NUMPAGES \\# "00" ')


def build_document(logos, tmp):
    doc = Document()
    word_styles(doc)
    sec = doc.sections[0]
    page_setup(sec)
    sec.different_first_page_header_footer = True
    header_footer(sec, logos)

    # Cover
    doc.add_paragraph().add_run().add_picture(str(logos["arsene-wordmark-ink"]), height=Mm(6))
    for _ in range(9):
        doc.add_paragraph()
    doc.add_paragraph("Titel van het document.", style="Title")
    doc.add_paragraph("Eén of twee zinnen die zeggen waar dit over gaat en voor wie het is. "
                      "Houd het kort: de rest van het document doet het werk.", style="Intro")
    for _ in range(10):
        doc.add_paragraph()
    doc.add_paragraph("Klant of project · 28 mei 2026 · Versie 1", style="Caption")
    doc.add_paragraph().add_run().add_break(WD_BREAK.PAGE)

    # Example content showing every style
    doc.add_paragraph("Inleiding.", style="Heading 1")
    doc.add_paragraph("Dit sjabloon volgt de Arsene-huisstijl. Alle opmaak zit in de stijlen, dus kies een stijl en "
                      "laat de knoppen voor lettertype, kleur en grootte met rust. Titels en koppen in zinsvorm; "
                      "een kop van niveau 1 eindigt met een punt.", style="Intro")
    doc.add_paragraph("De gewone tekst staat in de stijl Normal: Geist 10 punt in Warm 800. Schrijf droog en concreet, "
                      "spreek de lezer aan met jij en noem Arsene we. Geen em dash, geen emoji. Nadruk geef je met "
                      "woorden, niet met vet; vet is voor koppen.")
    doc.add_paragraph("Een blok met een lijn erboven", style="Heading 2")
    doc.add_paragraph("Kop 2 heeft een dunne lijn in Ink erboven, net als de blokken in het brand book. Gebruik hem "
                      "voor onderwerpen binnen een hoofdstuk.")
    doc.add_paragraph("Een kleine kop", style="Heading 3")
    doc.add_paragraph("Kop 3 is voor een groep alinea's of een opsomming:")
    for item in ("Begin elk punt met een hoofdletter.", "Een hele zin krijgt een punt.", "Houd het bij drie tot vijf punten."):
        doc.add_paragraph(item, style="List Bullet")
    doc.add_paragraph("Een tabel", style="Heading 2")
    rows = [("Dienst", "Uren", "Tarief (€)", "Totaal (€)"), ("Inventarisatie", "12", "95", "1.140"),
            ("Inrichting", "38", "95", "3.610"), ("Overdracht en uitleg", "6", "95", "570")]
    table = doc.add_table(rows=len(rows), cols=4)
    table.style = doc.styles["Arsene tabel"]
    table.alignment = WD_TABLE_ALIGNMENT.LEFT
    for r, row in enumerate(rows):
        for c, val in enumerate(row):
            cell = table.cell(r, c)
            cell.text = val
            if c:
                cell.paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.RIGHT
    doc.add_paragraph("Tabel 1. Een bijschrift staat in de stijl Caption, onder de tabel of figuur.", style="Caption")
    doc.add_paragraph("Grafieken", style="Heading 2")
    doc.add_paragraph("De themakleuren van dit sjabloon volgen de grafiekkleuren van de huisstijl: accent 1 tot 4 zijn "
                      "Mint Deep, oker, leiblauw en Mint. Een grafiek in Word kleurt daardoor vanzelf goed. "
                      "Gebruik er niet meer dan vier, of licht één reeks uit en zet de rest in accent 5 (warm grijs).")

    src = tmp / "document.docx"
    patch_word_theme(doc)
    doc.save(src)
    as_template(src, OUT / "Arsene_document.dotx", "/word/document.xml",
                "application/vnd.openxmlformats-officedocument.wordprocessingml.template.main+xml")


def patch_word_theme(doc):
    for rel in doc.part.rels.values():
        if rel.reltype.endswith("/theme"):
            rel.target_part._blob = theme_xml(rel.target_part.blob)


def build_letter(logos, tmp):
    doc = Document()
    word_styles(doc)
    sec = doc.sections[0]
    page_setup(sec, top=40)
    sec.header_distance = Mm(14)
    hp = sec.header.paragraphs[0]
    hp.add_run().add_picture(str(logos["arsene-wordmark-ink"]), height=Mm(6))
    fp = sec.footer.paragraphs[0]
    fp.style = "Lopende kop"
    fp.paragraph_format.tab_stops.add_tab_stop(Mm(174), WD_TAB_ALIGNMENT.RIGHT)
    fp.add_run("arsene.nl · info@arsene.nl\t")
    field(fp, ' PAGE \\# "00" ')
    fp.add_run(" / ")
    field(fp, ' NUMPAGES \\# "00" ')

    for line in ("[Naam ontvanger]", "[Organisatie]", "[Straat en huisnummer]", "[Postcode en plaats]"):
        p = doc.add_paragraph(line)
        p.paragraph_format.space_after = Pt(0)
    for _ in range(3):
        doc.add_paragraph()
    doc.add_paragraph("[Plaats], [datum voluit, bijvoorbeeld 28 mei 2026]", style="Caption")
    doc.add_paragraph("[Onderwerp in zinsvorm]", style="Heading 3")
    doc.add_paragraph()
    doc.add_paragraph("Beste [voornaam],")
    doc.add_paragraph("Begin met waar het om gaat. Wat wil je dat de lezer weet of doet? Zet dat in de eerste alinea, "
                      "en de uitleg daarna.")
    doc.add_paragraph("Schrijf zoals je praat: jij en we, korte zinnen, geen jargon. Eén onderwerp per alinea.")
    doc.add_paragraph("Met vriendelijke groet,")
    doc.add_paragraph()
    doc.add_paragraph("[Naam]", style="Heading 3")
    doc.add_paragraph("[Functie] · Arsene", style="Caption")

    src = tmp / "brief.docx"
    patch_word_theme(doc)
    doc.save(src)
    as_template(src, OUT / "Arsene_brief.dotx", "/word/document.xml",
                "application/vnd.openxmlformats-officedocument.wordprocessingml.template.main+xml")


# ---------------------------------------------------------------- PowerPoint

def a(tag):
    return f"{{{A}}}{tag}"


def text_style(lvl_ppr, size=None, bold=None, color=None, font=None, spc=None, caps=False, line=None, align=None):
    """Fill an <a:lvlNpPr> element: alignment, line spacing and default run properties."""
    for child in list(lvl_ppr):
        if child.tag in (a("lnSpc"), a("defRPr")):
            lvl_ppr.remove(child)
    if align:
        lvl_ppr.set("algn", align)
    if line:
        ln = etree.Element(a("lnSpc"))
        etree.SubElement(ln, a("spcPct"), val=str(int(line * 100000)))
        lvl_ppr.insert(0, ln)
    rpr = etree.SubElement(lvl_ppr, a("defRPr"))
    if size:
        rpr.set("sz", str(int(size * 100)))
    if bold is not None:
        rpr.set("b", "1" if bold else "0")
    if spc is not None:
        rpr.set("spc", str(int(spc)))
    if caps:
        rpr.set("cap", "all")
    if color:
        fill = etree.SubElement(rpr, a("solidFill"))
        etree.SubElement(fill, a("srgbClr"), val=hexval(color))
    if font:
        etree.SubElement(rpr, a("latin"), typeface=font)


def ph_style(ph, **kw):
    tx = ph._element.txBody
    lst = tx.find(a("lstStyle"))
    if lst is None:
        lst = etree.Element(a("lstStyle"))
        tx.insert(1, lst)
    lvl = lst.find(a("lvl1pPr"))
    if lvl is None:
        lvl = etree.SubElement(lst, a("lvl1pPr"))
    text_style(lvl, **kw)


def clear_lst(ph):
    """Drop a layout placeholder's own list style, so the master text styles apply."""
    lst = ph._element.txBody.find(a("lstStyle"))
    if lst is not None:
        for child in list(lst):
            lst.remove(child)


def place(shape, x, y, w, h):
    shape.left, shape.top, shape.width, shape.height = Inches(x), Inches(y), Inches(w), Inches(h)


def bg(slide_like, color):
    fill = slide_like.background.fill
    fill.solid()
    from pptx.dml.color import RGBColor as PRGB
    fill.fore_color.rgb = PRGB.from_string(hexval(color))


def add_picture_to(prs, target, png, x, y, h):
    """Layouts and masters cannot add pictures directly: add on a scratch slide and move it."""
    scratch = prs.slides.add_slide(prs.slide_layouts[0])
    pic = scratch.shapes.add_picture(str(png), Inches(x), Inches(y), height=Inches(h))
    blip = pic._element.find(".//" + a("blip"))
    rid = blip.get(qn("r:embed"))
    image_part = scratch.part.related_part(rid)
    blip.set(qn("r:embed"), target.part.relate_to(image_part, RT.IMAGE))
    target.shapes._spTree.append(pic._element)
    sld_ids = prs.slides._sldIdLst
    last = sld_ids[-1]
    prs.part.drop_rel(last.rId)
    sld_ids.remove(last)


def rename(layout, name):
    layout._element.cSld.set("name", name)


def phs(layout):
    return {ph.placeholder_format.type: ph for ph in layout.placeholders}


def drop(shape):
    shape._element.getparent().remove(shape._element)


def build_presentation(logos, tmp):
    prs = Presentation()
    prs.slide_width, prs.slide_height = Inches(13.333), Inches(7.5)
    master = prs.slide_master
    rel = master.part.part_related_by(RT.THEME)
    rel._blob = theme_xml(rel.blob)

    # Master: paper, Geist, warm-800 body, running head top, wordmark bottom left
    bg(master, "paper")
    tx = master._element.find(pqn("p:txStyles"))
    text_style(tx.find(pqn("p:titleStyle")).find(a("lvl1pPr")), size=36, bold=True, color="ink", spc=-140, line=0.95, align="l")
    body = tx.find(pqn("p:bodyStyle"))
    for i, size in ((1, 20), (2, 18), (3, 16), (4, 14), (5, 14)):
        text_style(body.find(a(f"lvl{i}pPr")), size=size, color="warm-800", line=1.2)
    M = 0.75
    for ph in master.placeholders:
        t = ph.placeholder_format.type
        if t == PP_PLACEHOLDER.TITLE:
            place(ph, M, 0.95, 11.8, 1.2)
        elif t == PP_PLACEHOLDER.BODY:
            place(ph, M, 2.35, 11.8, 4.2)
        elif t == PP_PLACEHOLDER.FOOTER:
            place(ph, M, 0.4, 8, 0.3)
            ph_style(ph, size=10, color="warm-600", font=MONO, caps=True, spc=80, align="l")
        elif t == PP_PLACEHOLDER.SLIDE_NUMBER:
            place(ph, 13.333 - M - 2, 0.4, 2, 0.3)
            ph_style(ph, size=10, color="warm-600", font=MONO, align="r")
        elif t == PP_PLACEHOLDER.DATE:
            place(ph, 13.333 - M - 3, 6.85, 3, 0.3)
            ph_style(ph, size=10, color="warm-600", font=MONO, align="r")
    add_picture_to(prs, master, logos["arsene-wordmark-ink"], M, 6.88, 0.24)

    L = list(prs.slide_layouts)
    title, content, section, two, comparison, title_only, blank, content_cap, pic_cap, vert1, vert2 = L
    for lay in (vert1, vert2):
        prs.slide_layouts.remove(lay)

    def teal(layout, name):
        rename(layout, name)
        bg(layout, "teal-deep")
        layout._element.cSld.getparent().set("showMasterSp", "0")
        add_picture_to(prs, layout, logos["arsene-wordmark-paper"], M, 0.62, 0.3)
        for ph in layout.placeholders:
            t = ph.placeholder_format.type
            if t in (PP_PLACEHOLDER.FOOTER, PP_PLACEHOLDER.SLIDE_NUMBER, PP_PLACEHOLDER.DATE):
                ph_style(ph, size=10, color="teal-fg", font=MONO, caps=t == PP_PLACEHOLDER.FOOTER,
                         align="l" if t == PP_PLACEHOLDER.FOOTER else "r")
                if t == PP_PLACEHOLDER.FOOTER:
                    place(ph, M + 2.2, 0.62, 6, 0.3)

    # Titel
    teal(title, "Titel")
    p = phs(title)
    place(p[PP_PLACEHOLDER.CENTER_TITLE], M, 2.3, 11, 2.4)
    ph_style(p[PP_PLACEHOLDER.CENTER_TITLE], size=66, bold=True, color="teal-fg", spc=-300, line=0.9, align="l")
    p[PP_PLACEHOLDER.CENTER_TITLE]._element.txBody.bodyPr.set("anchor", "b")
    place(p[PP_PLACEHOLDER.SUBTITLE], M, 4.9, 8.5, 1.2)
    ph_style(p[PP_PLACEHOLDER.SUBTITLE], size=20, color="teal-fg", line=1.3, align="l")

    # Titel en inhoud, Twee kolommen, Vergelijking, Alleen titel, Leeg
    rename(content, "Titel en inhoud")
    for lay in (content, two, comparison):
        for ph in lay.placeholders:
            if ph.placeholder_format.type == PP_PLACEHOLDER.OBJECT:
                clear_lst(ph)
    rename(two, "Twee kolommen")
    p = phs(two)
    objs = [ph for ph in two.placeholders if ph.placeholder_format.type == PP_PLACEHOLDER.OBJECT]
    for i, ph in enumerate(objs):
        place(ph, M + i * 6.1, 2.35, 5.7, 4.2)
    rename(comparison, "Vergelijking")
    bodies = [ph for ph in comparison.placeholders if ph.placeholder_format.type == PP_PLACEHOLDER.BODY]
    objs = [ph for ph in comparison.placeholders if ph.placeholder_format.type == PP_PLACEHOLDER.OBJECT]
    for i, ph in enumerate(bodies):
        place(ph, M + i * 6.1, 2.35, 5.7, 0.5)
        ph_style(ph, size=16, bold=False, color="ink", font=SEMI)
    for i, ph in enumerate(objs):
        place(ph, M + i * 6.1, 2.95, 5.7, 3.6)
    rename(title_only, "Alleen titel")
    rename(blank, "Leeg")

    # Sectie
    teal(section, "Sectie")
    p = phs(section)
    place(p[PP_PLACEHOLDER.TITLE], M, 2.2, 11, 2.4)
    ph_style(p[PP_PLACEHOLDER.TITLE], size=60, bold=True, color="teal-fg", spc=-270, line=0.9, align="l")
    p[PP_PLACEHOLDER.TITLE]._element.txBody.bodyPr.set("anchor", "b")
    place(p[PP_PLACEHOLDER.BODY], M, 4.8, 8.5, 1.0)
    ph_style(p[PP_PLACEHOLDER.BODY], size=20, color="teal-fg", line=1.3, align="l")

    # Statement (was Inhoud met bijschrift): one big sentence on paper
    rename(content_cap, "Statement")
    for ph in list(content_cap.placeholders):
        t = ph.placeholder_format.type
        if t == PP_PLACEHOLDER.OBJECT:
            drop(ph)
        elif t == PP_PLACEHOLDER.TITLE:
            place(ph, M, 1.6, 11.5, 3.6)
            ph_style(ph, size=54, bold=True, color="ink", spc=-240, line=0.95, align="l")
            ph._element.txBody.bodyPr.set("anchor", "b")
        elif t == PP_PLACEHOLDER.BODY:
            place(ph, M, 5.45, 8.5, 0.8)
            ph_style(ph, size=18, color="warm-800", line=1.3, align="l")

    # Afsluiting (was Afbeelding met bijschrift): teal, tagline and contact
    teal(pic_cap, "Afsluiting")
    for ph in list(pic_cap.placeholders):
        t = ph.placeholder_format.type
        if t == PP_PLACEHOLDER.PICTURE:
            drop(ph)
        elif t == PP_PLACEHOLDER.TITLE:
            place(ph, M, 2.0, 11, 3.0)
            ph_style(ph, size=88, bold=True, color="teal-fg", spc=-400, line=0.88, align="l")
            ph._element.txBody.bodyPr.set("anchor", "b")
        elif t == PP_PLACEHOLDER.BODY:
            place(ph, M, 5.4, 8.5, 0.9)
            ph_style(ph, size=18, color="teal-fg", line=1.3, align="l")

    # Order: Titel, Sectie, Titel en inhoud, Twee kolommen, Vergelijking, Statement, Alleen titel, Leeg, Afsluiting
    lst = master._element.find(pqn("p:sldLayoutIdLst"))
    by_part = {master.part.related_part(e.get(qn("r:id"))): e for e in lst}
    order = [title, section, content, two, comparison, content_cap, title_only, blank, pic_cap]
    for lay in order:
        el = by_part[lay.part]
        lst.remove(el)
        lst.append(el)

    # Example slides, one per layout
    def slide(layout, title_text=None, body=None, extra=None):
        s = prs.slides.add_slide(layout)
        for ph in s.placeholders:
            t = ph.placeholder_format.type
            if t in (PP_PLACEHOLDER.TITLE, PP_PLACEHOLDER.CENTER_TITLE) and title_text:
                ph.text = title_text
            elif t in (PP_PLACEHOLDER.SUBTITLE, PP_PLACEHOLDER.BODY, PP_PLACEHOLDER.OBJECT) and body:
                ph.text = body.pop(0) if isinstance(body, list) else body
                if not isinstance(body, list):
                    body = None
        return s

    slide(title, "Titel van de presentatie.", "Eén zin die zegt waar het over gaat.")
    slide(section, "Een nieuw hoofdstuk.", "Een korte toelichting, of laat dit vak leeg.")
    slide(content, "Titel en inhoud.", "Begin met de conclusie. Daarna de uitleg, in korte punten.\nHoogstens vijf punten per dia.\nZinsvorm, geen em dash, geen emoji.")
    slide(two, "Twee kolommen.", ["Links het een.", "Rechts het ander."])
    s = prs.slides.add_slide(comparison)
    s.shapes.title.text = "Vergelijking."
    heads = sorted((ph for ph in s.placeholders if ph.placeholder_format.type == PP_PLACEHOLDER.BODY), key=lambda ph: ph.left)
    cols = sorted((ph for ph in s.placeholders if ph.placeholder_format.type == PP_PLACEHOLDER.OBJECT), key=lambda ph: ph.left)
    for ph, text in zip(heads, ("Nu", "Straks")):
        ph.text = text
    for ph, text in zip(cols, ("Zes Excels, handmatig bijgewerkt.", "Eén dashboard dat zichzelf bijwerkt.")):
        ph.text = text
    slide(content_cap, "Software op jouw voorwaarden.", "Eén zin, groot. Voor de boodschap die moet blijven hangen.")
    slide(title_only, "Alleen titel.")
    slide(pic_cap, "alles kan.", "arsene.nl · info@arsene.nl")

    src = tmp / "presentatie.pptx"
    prs.save(src)
    as_template(src, OUT / "Arsene_presentatie.potx", "/ppt/presentation.xml",
                "application/vnd.openxmlformats-officedocument.presentationml.template.main+xml")


def main():
    OUT.mkdir(exist_ok=True)
    with tempfile.TemporaryDirectory() as t:
        tmp = Path(t)
        logos = logo_pngs(tmp)
        build_document(logos, tmp)
        build_letter(logos, tmp)
        build_presentation(logos, tmp)
    for f in sorted(OUT.glob("Arsene_*")):
        print("wrote", f.relative_to(ROOT))


if __name__ == "__main__":
    main()
