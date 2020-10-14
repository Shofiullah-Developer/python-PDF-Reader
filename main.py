import pyttsx3 as py
import PyPDF2
pdf =open('mlpy.pdf','rb')
pdfReader =PyPDF2.PdfFileReader(pdf)
pages =pdfReader.numPages
print(pages)
a = py.init()
for num in range(5,pages):
    page =pdfReader.getPage(num)
    text = page.extractText()
    a.say(text)
    a.runAndWait()