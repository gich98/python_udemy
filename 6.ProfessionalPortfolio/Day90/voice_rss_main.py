import PyPDF2   # Module to extract text from the pdf
import webbrowser   # Module to open the browser


KEY = 'MY_PERSONAL_KEY_VOICE_RSS'
LANGUAGE = 'en-us'
VOICE = 'Mary'
pdf_name = 'TestReadPDF.pdf'
# create file object variable
# opening method will be rb
pdf_file = open(pdf_name, 'rb')

# create reader variable that will read the pdf_file
pdfreader = PyPDF2.PdfFileReader(pdf_file)

# This will store the number of pages of this pdf file
# (num_pages - 1) because python indentation starts with 0.
num_pages = pdfreader.numPages - 1
# create a variable that will select the selected number of pages
page_pdf = pdfreader.getPage(num_pages)

# create text variable which will store all text data from pdf file
text = page_pdf.extractText()

webbrowser.open(f'http://api.voicerss.org/?key={KEY}&hl={LANGUAGE}&v={VOICE}&src={text}')
