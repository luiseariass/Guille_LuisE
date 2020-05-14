import PyPDF2


bg_filename = 'draft.pdf'
fg_filename = 'original.pdf'
out_filename = 'Merged.pdf'

with open(bg_filename, 'rb') as bg_file, open(fg_filename, 'rb') as fg_file:
    bg_page = PyPDF2.PdfFileReader(bg_file).getPage(0)
    pdf_out = PyPDF2.PdfFileWriter()
    fg_reader = PyPDF2.PdfFileReader(fg_file)
    fg_pages = [fg_reader.getPage(i) for i in range(fg_reader.getNumPages())]
    print(fg_pages)
    for page in fg_pages:
        if page.extractText():  # Do not copy pages that have no text
            page.mergePage(bg_page)
            pdf_out.addPage(page)
    if pdf_out.getNumPages():
        with open(out_filename, 'wb') as out_file:
            # Caution: All three files MUST be open when write() is called
            pdf_out.write(out_file)