# tools/pdf_to_docx_converter.py

from pdf2docx import Converter, parse
from PyPDF2 import PdfReader, PdfWriter

def pdf_to_docx_converter(pdf_file_path, output_docx_path):
    try:
        # Convert the PDF file to DOCX
        cv = Converter(pdf_file_path)
        cv.convert(output_docx_path)
        cv.close()
        # parse(pdf_file_path,output_docx_path)
        return True, None
    # except:
        # parse(pdf_file_path,output_docx_path)
    except Exception as e:
        return False, str(e)


# # Extract Text from a PDF

# reader = PdfReader("rsrrules.pdf")
# page = reader.pages[0]
# # extract only text oriented up
# print(page.extract_text())
# # extract text oriented up and turned left
# print(page.extract_text((0, 90)))



# def pdf_to_docx_converter(pdf_file_path, output_docx_path):
#     try:
        # reader = PdfReader(pdf_file_path)
# reader = PdfReader("./rsrrules1.pdf")
# print("Reader working")
# writer = PdfWriter()
# for page in reader.pages:
#     writer.add_page(page)

# writer.add_metadata(reader.metadata)
# # Converter(writer, )print(f"Type of writer {type(writer)}")
# with open("smaller-new-file.pdf", "wb") as fp:
#     writer.write(fp)        
# # Convert the PDF file to DOCX
# y = PdfReader('./smaller-new-file.pdf')
# cv = Converter(y)
# compressed = './smaller.pdf'
# cv.convert(compressed)
# cv.close()
        # return True, None

#     except Exception as e:
#         return False, str(e)


# pdf_to_docx_converter('.rsrrules1.pdf', './')
