import PyPDF2
import os

with open(f'{os.path.abspath(os.getcwd())}\\scripting\\pdf_playground\\dummy.pdf', 'rb') as file:
    reader = PyPDF2.PdfReader(file)
    page = reader.pages[0]
    # print(page.rotate(90))
    page.rotate(-90)
    writer = PyPDF2.PdfWriter()
    writer.add_page(page)

    with open(f'{os.path.abspath(os.getcwd())}\\scripting\\pdf_playground\\tilt.pdf', 'wb') as new_file:
        writer.write(new_file)
