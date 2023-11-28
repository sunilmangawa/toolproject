# from PyPDF2 import PdfReader, PdfWriter

# reader = PdfReader("rsrrules1.pdf")
# writer = PdfWriter()

# for page in reader.pages:
#     writer.add_page(page)

# writer.add_metadata(reader.metadata)

# with open("smaller-new-file.pdf", "wb") as fp:
#     writer.write(fp)



from PyPDF2 import PdfReader, PdfWriter
from pdf2docx import Converter
# reader = PdfReader("bookdj.pdf")
# reader = PdfReader("rsrrules.pdf")
writer = PdfWriter()

# for page in reader.pages:
#     page.compress_content_streams()  # This is CPU intensive!
#     writer.add_page(page)

# with open("compressed book.pdf", "wb") as f:
#     writer.write(f)

reader = PdfReader("rsrrules.pdf")
for page in reader.pages:
    page.extract_text()
    writer.add_page(page)
with open("compressed book.pdf", "wb") as f:
    writer.write(f)
cv = Converter("compressed book.pdf")
cv.convert("compressed book.docx")
cv.close()
# page = reader.pages[:]
# print(page.extract_text())

# pdf_file = './rsrrules.pdf'
# docx_file = './sample.docx'

# # convert pdf to docx
# cv = Converter(pdf_file)
# cv.convert(docx_file)      # all pages by default
# cv.close()

# from pdfminer.high_level import extract_text
# from docx import Document

# pdf_file = './rsrrules.pdf'
# docx_file = './sample.docx'

# def pdf_to_docx_converter(pdf_file_path, output_docx_path):
#     # try:
#     # Extract text from the PDF
#     pdf_text = extract_text(pdf_file_path)

#     # Create a new DOCX document
#     doc = Document()
#     doc.add_paragraph(pdf_text)

#     # Save the DOCX file
#     doc.save(output_docx_path)

#     #     return True, None
#     # except Exception as e:
#     #     return False, str(e)

# pdf_to_docx_converter(pdf_file, docx_file)

# # Successful to convert and get text but not with same formatting.
# from pdfminer.high_level import extract_text
# from docx import Document
# import re

# def clean_text_for_xml(text):
#     # Remove characters that are not XML-compatible
#     return re.sub(r'[^\x20-\x7E]', '', text)

# def pdf_to_docx_converter(pdf_file_path, output_docx_path):
#     try:
#         # Extract text from the PDF
#         pdf_text = extract_text(pdf_file_path)

#         # Clean the text for XML compatibility
#         cleaned_text = clean_text_for_xml(pdf_text)

#         # Create a new DOCX document
#         doc = Document()
#         doc.add_paragraph(cleaned_text)

#         # Save the DOCX file
#         doc.save(output_docx_path)

#         return True, None
#     except Exception as e:
#         return False, str(e)

# # Example usage
# pdf_file = './rsrrules.pdf'
# docx_file = './sample.docx'
# pdf_to_docx_converter(pdf_file, docx_file)


# import fitz  # PyMuPDF
# from docx import Document

# def pdf_to_docx_converter(pdf_file_path, output_docx_path):
#     try:
#         # Open the PDF file
#         pdf_document = fitz.open(pdf_file_path)

#         # Create a new DOCX document
#         doc = Document()

#         for page_number in range(pdf_document.page_count):
#             # Extract text and formatting information from the PDF page
#             pdf_page = pdf_document[page_number]
#             pdf_text = pdf_page.get_text("text")
#             pdf_blocks = pdf_page.get_text("blocks")

#             # Add each block of text to the DOCX document with formatting
#             for block in pdf_blocks:
#                 text = block[4]  # Extract the text content
#                 font_size = block[1]  # Extract the font size

#                 # Set the font size in the style of the paragraph
#                 style = doc.styles['Normal']
#                 style.font.size = Pt(font_size)

#                 # Add a paragraph with the extracted text and style
#                 paragraph = doc.add_paragraph(text, style)

#         # Save the DOCX file
#         doc.save(output_docx_path)

#         return True, None
#     except Exception as e:
#         return False, str(e)

# # Example usage
# pdf_file = './rsrrules.pdf'
# docx_file = './sample.docx'
# pdf_to_docx_converter(pdf_file, docx_file)
