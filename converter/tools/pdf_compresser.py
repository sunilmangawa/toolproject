# from PyPDF2 import PdfReader, PdfWriter

# reader = PdfReader("rsrrules1.pdf")
# writer = PdfWriter()

# for page in reader.pages:
#     writer.add_page(page)

# writer.add_metadata(reader.metadata)

# with open("smaller-new-file.pdf", "wb") as fp:
#     writer.write(fp)



from PyPDF2 import PdfReader, PdfWriter

# reader = PdfReader("bookdj.pdf")
reader = PdfReader("rsrrules1.pdf")
writer = PdfWriter()

for page in reader.pages:
    page.compress_content_streams()  # This is CPU intensive!
    writer.add_page(page)

with open("compressed book.pdf", "wb") as f:
    writer.write(f)