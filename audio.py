#importing pyttsx3 library 
import pyttsx3
#pyttsx3 is a text-to-speech conversion library in Python.
#importing PyPDF2 library
import PyPDF2
# PyPDF2 is used for:-
#extracting document information (title, author, …)
#splitting documents page by page
#merging documents page by page
#cropping pages
#merging multiple pages into a single page
#encrypting and decrypting PDF files
pdf=open('Aboutpython.pdf','rb')
#open the book to be audit
pdfread=PyPDF2.PdfFileReader(pdf)
#PdfFileReader is used to read the pdf
pages=pdfread.numPages
print(pages)
#.numPages is used to print the number of pages
Bot=pyttsx3.init()
#init is used to  initialization to get Bot ready to perform
page=pdfread.getPage(0)
text=page.extractText()
#.getPage(PAGE NUMBER ) is used to audit a particular page
Bot.say(text)
#.say is used to get output in form of speech from the bot
Bot.runAndWait()
