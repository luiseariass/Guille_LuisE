from PyPDF2 import PdfFileWriter, PdfFileReader
from PyPDF2 import PdfFileWriter, PdfFileReader
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, A4
def write_in_pdf (name_input,name_outpout,Manager,firma,observaciones=""):
	packet = io.BytesIO()
	# create a new PDF with Reportlab
	can = canvas.Canvas(packet, pagesize=A4)
	can.drawString(5, -50, "Firma manager: %s"%Manager)
	can.drawString(270,-50,"Observaciones: %s"%observaciones)
	can.drawImage(firma, 200, -50, width=50, height=30)
	can.save()

	#move to the beginning of the StringIO buffer
	packet.seek(0)
	new_pdf = PdfFileReader(packet)
	# read your existing PDF
	existing_pdf = PdfFileReader(open(name_input, "rb"))
	output = PdfFileWriter()
	# add the "watermark" (which is the new pdf) on the existing page
	page = existing_pdf.getPage(0)
	page.mergePage(new_pdf.getPage(0))
	output.addPage(page)
	# finally, write "output" to a real file
	outputStream = open(name_outpout, "wb")
	output.write(outputStream)
	outputStream.close()

def add_margin (name_input,name_outpout):

	pdf = PdfFileReader(open('original.pdf', 'rb'))
	p = pdf.getPage(0)
	for box in (p.mediaBox, p.cropBox, p.bleedBox,
                                    p.trimBox, p.artBox):
    		box.lowerLeft = (box.getLowerLeft_x() - 0,
                     box.getLowerLeft_y() - 60)
    		box.upperRight = (box.getUpperRight_x() + 0,
                      box.getUpperRight_y() + 0)
	output = PdfFileWriter()
	output.addPage(p)
	output.write(open(name_outpout, 'wb'))

add_margin("original.pdf","copia.pdf")
write_in_pdf('copia.pdf','copia2.pdf',"Luis Enrique Arias","draft.png")