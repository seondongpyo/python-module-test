import os

from PyPDF2 import PdfFileReader, PdfFileWriter

# PyPDF2 documentation : https://pythonhosted.org/PyPDF2/index.html

sample_pdf_file = os.getcwd() + '\\sample.pdf'

# PDF 파일 열기
pdf = PdfFileReader(open(sample_pdf_file, 'rb'))

# PDF 파일의 페이지 수 구하기
pdf_pages = pdf.getNumPages()

# PDF 파일의 정보 가져오기
pdf_info = pdf.getDocumentInfo()
title = pdf_info.title
creator = pdf_info.creator
producer = pdf_info.producer
author = pdf_info.author

# 첫 페이지의 텍스트 추출하기
first_page = pdf.getPage(0)
first_page_text = first_page.extractText()

# 첫 페이지의 내용으로 새로운 PDF 파일 생성하기
pdf_writer = PdfFileWriter()
pdf_writer.addPage(first_page)
new_pdf_file_name = 'new.pdf'
new_pdf_file_path = os.path.join(os.getcwd(), new_pdf_file_name)

with open(new_pdf_file_path, 'wb') as new_pdf_file:
    pdf_writer.write(new_pdf_file)
