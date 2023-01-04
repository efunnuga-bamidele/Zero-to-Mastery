import PyPDF2
import os
import sys

template = PyPDF2.PdfReader(open(f'{os.path.abspath(os.getcwd())}\\scripting\\pdf_playground\\resume.pdf', 'rb'))
watermark = PyPDF2.PdfReader(open(f'{os.path.abspath(os.getcwd())}\\scripting\\pdf_playground\\wtr.pdf', 'rb'))
output = PyPDF2.PdfWriter()

for i in range(len(template.pages)):
    page = template.pages[i]
    page.merge_page(watermark.pages[0])
    output.add_page(page)

    with open(f'{os.path.abspath(os.getcwd())}\\scripting\\pdf_playground\\watermarked_output.pdf', 'wb') as file:
        output.write(file)