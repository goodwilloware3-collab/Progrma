import PyPDF2
import os
#initialize pyPDF2 PdfMerger object
merger=PyPDF2.PdfMerger()
for filename in os.listdir():
    if filename.endswith('.pdf'):
        merger.append(filename)
merger.write('merged.pdf')
merger.close()
print("PDF files merged successfully into 'merged.pdf'")
#"C:\Users\HP\Desktop\Progrmaming\Python\PDFmerger"