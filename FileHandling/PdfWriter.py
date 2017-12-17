from PyPDF2 import PdfFileWriter, PdfFileReader

writer=PdfFileWriter()
outfp=open("outpath",'wb')
writer.write(outfp)
