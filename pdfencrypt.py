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
parser.add_argument('--owner', metavar='passphrase', help='Set owner password', default=generatepassword(12))
parser.add_argument('--user', metavar='passphrase', help='Set user password', default=generatepassword(12))

args = parser.parse_args(args=None if sys.argv[1:] else ['--help'])
print(args.pdffile.name)
print(args)
try:
    pdfReader = PyPDF3.PdfFileReader(args.pdffile,strict=False)
except Exception as errormsg:
    print(errormsg)
    sys.exit(1)
# need a check for already encrypted file
if (args.output):
    output = args.output
else:
    ospathsplit = os.path.splitext(args.pdffile.name)
    output = f"{ospathsplit[0]} - encrypted{ospathsplit[1]}"
# args.pdffile.close()
print(output)

pdfWriter = PyPDF3.PdfFileWriter()
for page in range(pdfReader.numPages):
    pdfWriter.addPage(pdfReader.getPage(page))
pdfWriter.encrypt(user_pwd=args.user,owner_pwd=args.owner)
try:
    resultpdf = open(output, 'wb')
    pdfWriter.write(resultpdf)
except Exception as errormsg:
    print(errormsg)

    
resultpdf.close
args.pdffile.close