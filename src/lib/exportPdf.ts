import html2canvas from 'html2canvas';
import jsPDF from 'jspdf';

export async function exportPdf() {
  await document.fonts.ready;

  const pages = Array.from(document.querySelectorAll<HTMLElement>('.page'));
  const pdf = new jsPDF({ unit: 'mm', format: 'a4', orientation: 'portrait' });

  for (let i = 0; i < pages.length; i++) {
    const canvas = await html2canvas(pages[i], {
      scale: 2,
      useCORS: true,
      backgroundColor: null,
    });

    if (i > 0) pdf.addPage();
    pdf.addImage(canvas.toDataURL('image/png'), 'PNG', 0, 0, 210, 297);
  }

  pdf.save('arsene-huisstijl.pdf');
}
