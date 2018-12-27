from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.cidfonts import UnicodeCIDFont
import reportlab.lib.units as unit
import reportlab.lib.pagesizes as pagesizes

pdfmetrics.registerFont(UnicodeCIDFont('HeiseiKakuGo-W5'))

pdf = canvas.Canvas('pytest84.pdf', pagesize=pagesizes.A4)

title = '新春セール！'
for moji in title:
    # char size,same as pp width
    pdf.setFont('HeiseiKakuGo-W5', 210*unit.mm)
    # char height
    # To centerise, (H - fontSize/2)
    h = (297-210)/2*unit.mm # ここが底辺
    # vars are availible!!!
    pdf.drawString(0*unit.mm, h, moji)
    pdf.showPage()

# A4 is width = 210mm, height = 297mm.
pdf.save()

