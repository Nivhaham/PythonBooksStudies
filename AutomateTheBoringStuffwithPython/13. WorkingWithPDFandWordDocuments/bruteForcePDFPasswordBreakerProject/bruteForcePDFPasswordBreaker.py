# The pdf will be encrypted using the word: "biotechnology"
import PyPDF2


def encryptPDF():
    # with open('Secret.pdf', 'rb') as pdfFile:
    with open('Secret100.pdf', 'rb') as pdfFile:
        pdfReader = PyPDF2.PdfReader(pdfFile)
        # print(pdfReader.pages[0].values())
        pdfWriter = PyPDF2.PdfWriter()
        for pageNum in range(len(pdfReader.pages)):
            page = pdfReader.pages[pageNum]
            #print(page)
            pdfWriter.add_page(page)
        with open('Secret101.pdf', 'wb') as resultPdf:
            pdfWriter = PyPDF2.PdfWriter()
            pdfWriter.encrypt('biotechnology', 'biotechnology')
            pdfWriter.write(resultPdf)


def tryDecrypt(fileToDecrypt):
    with open(fileToDecrypt, 'rb') as pdfFile:
        pdfReader = PyPDF2.PdfReader(pdfFile)
        with open('google-10000-english.txt', 'rb') as passwordsFile:
            for password in passwordsFile.readlines():
                if pdfReader.decrypt(password) == 1:
                    print(password)
                    break
    return password

def main():
    encryptPDF()
    tryDecrypt('encryptedSecret.pdf')


if __name__ == '__main__':
    main()
