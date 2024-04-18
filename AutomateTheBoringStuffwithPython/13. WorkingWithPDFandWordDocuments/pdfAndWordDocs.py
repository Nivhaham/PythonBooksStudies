import PyPDF2
import docx
'''
The Problematic PDF Format
While PDF files are great for laying out text in a way that’s easy for people to
print and read, they’re not straightforward for software to parse into plaintext.
As such, PyPDF2 might make mistakes when extracting text from a PDF and
may even be unable to open some PDFs at all. There isn’t much you can do
about this, unfortunately. PyPDF2 may simply be unable to work with some of
your particular PDF files. That said, I haven’t found any PDF files so far that
can’t be opened with PyPDF2.
'''
'''
PyPDF2 does not have a way to extract images, charts, or other media from
PDF documents, but it can extract text and return it as a Python string
'''

'''
The PDF section is not very interesting you can 
work with PDF Object to read from PDF or Write to PDF


PyPDF2 can also overlay the contents of one page over another, which is
useful for adding a logo, timestamp, or watermark to a page.
There is also an encrypt method to encrypt a pdf
'''


#------------------------------------------------------------------------------------------

'''
Python can create and modify Word documents, which have the .docx file
extension, with the python-docx module.

In Word for Windows: 
.docx files have a lot of structure. This structure
is represented by three different data types in Python-Docx. 
At the highest level, a Document object represents the entire document.
The Document object contains a list of Paragraph objects for the paragraphs in the document.
(A new paragraph begins whenever the user presses enter or return while
typing in a Word document.) 
Each of these Paragraph objects contains a list of one or more Run objects.
'''

'''
The text in a Word document is more than just a string. It has font, size,
color, and other styling information associated with it. A style in Word is a
collection of these attributes. A Run object is a contiguous run of text with
the same style. A new Run object is needed whenever the text style changes.
'''