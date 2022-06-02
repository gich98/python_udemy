from gtts import gTTS   # Module of Google to convert text to speech
import os   # Module to use the os functionality, in our case to run iTunes
import PyPDF2   # Module to extract text from the pdf


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

# Language in which you want to convert
language = 'en'

# Passing the text and language to the engine,
# here we have marked slow=False. Which tells
# the module that the converted audio should
# have a high speed
gtss_obj = gTTS(text=text, lang=language, slow=False)

# Saving the converted audio in a mp3 file named
# welcome
gtss_obj.save(f"{pdf_name}.mp3")

# Playing the converted file
os.system(f"iTunes.exe {pdf_name}.mp3")
