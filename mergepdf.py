import os
from PyPDF2 import PdfReader, PdfWriter

def merge_pdfs(input_folder, output_filename):
    pdf_writer = PdfWriter()

    # Loop through all the files in the folder
    for filename in sorted(os.listdir(input_folder)):
        if filename.endswith('.pdf'):
            filepath = os.path.join(input_folder, filename)
            pdf_reader = PdfReader(filepath)
            for page_num in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_num]
                pdf_writer.add_page(page)

    # Write out the merged PDF
    with open(output_filename, 'wb') as output_pdf:
        pdf_writer.write(output_pdf)

if __name__ == "__main__":
    input_folder = '.'  # Replace with the path to your folder
    output_filename = 'merged_document.pdf'  # Output filename for the merged PDF
    merge_pdfs(input_folder, output_filename)
    print(f'Merged PDF saved as {output_filename}')
