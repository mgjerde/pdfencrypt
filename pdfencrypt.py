import secrets
import string
import PyPDF3
import os.path
import sys
import argparse

def generatepassword(length):
    return secrets.token_urlsafe(length)

parser = argparse.ArgumentParser(description='Encrypt R Us', usage='%(prog)s filename [options]')
parser.add_argument('pdffile', metavar='filename', type=argparse.FileType('rb'), help='The file you want to encrypt')
# parser.add_argument('-i', '--interactive', action='store_true', help='Function to interactivly help with the inputs')
parser.add_argument('-o', '--output', metavar='filename', help='Save the encrypted PDF file as this')
parser.add_argument('--owner', metavar='passphrase', help='Set owner password')
parser.add_argument('--user', metavar='passphrase', help='Set user password')

args = parser.parse_args(args=None if sys.argv[1:] else ['--help'])


try:
    pdfReader = PyPDF3.PdfFileReader(args.pdffile,strict=False)
except Exception as errormsg:
    print(errormsg)
    sys.exit(1)


print(generatepassword(12))

# args.pdffile.close()


print('Argument List:', args )


def encryptPDF(pdffil, userpwd=None, ownerpwd=None):
    
    pdfReader = PyPDF3.PdfFileReader(pdffil)
   
    pdfWriter = PyPDF3.PdfFileWriter()
    for page in range(pdfReader.numPages):
        pdfWriter.addPage(pdfReader.getPage(page))
    pdfWriter.encrypt(user_pwd=userpwd,owner_pwd=ownerpwd)
    resultpdf = open(f'encrypted.pdf', 'wb')
    pdfWriter.write(resultpdf)
    
    resultpdf.close



# import PyPDF2
# pdfFile = open('input.pdf', 'rb')
# # Create reader and writer object
# pdfReader = PyPDF2.PdfFileReader(pdfFile)
# pdfWriter = PyPDF2.PdfFileWriter()
# # Add all pages to writer (accepted answer results into blank pages)
# for pageNum in range(pdfReader.numPages):
#     pdfWriter.addPage(pdfReader.getPage(pageNum))
# # Encrypt with your password
# pdfWriter.encrypt('password')
# # Write it to an output file. (you can delete unencrypted version now)
# resultPdf = open('encrypted_output.pdf', 'wb')
# pdfWriter.write(resultPdf)
# resultPdf.close()
# Create the root window