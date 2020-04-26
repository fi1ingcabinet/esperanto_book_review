import PyPDF2
import collections
pdf_file = open('/users/petercurrie/Desktop/stuff/memory/esperanto/eo - bronte, charlotte - jane eyre 2.pdf', 'rb')
read_pdf = PyPDF2.PdfFileReader(pdf_file)
number_of_pages = read_pdf.getNumPages()
c = collections.Counter(range(number_of_pages))
for i in c:
   page = read_pdf.getPage(i)
   page_content = page.extractText()
   print(page_content.encode('utf-8'))
