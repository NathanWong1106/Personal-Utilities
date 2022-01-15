"""
Util to split a pdf into pages

Dependencies:
    PyPDF2 (pip install pypdf2)
    Tkinter

Usage:
    1) Choose your pdf file for the first input prompt
    2) Choose the folder that you would like the new pages to be stored in 
    3) Pray it doesn't crash
    4) Enjoy
"""

import os
from tkinter.filedialog import askdirectory, askopenfilename
from  PyPDF2 import PdfFileReader, PdfFileWriter

WIN_PDF_EXTENSION = ".pdf"
GENERIC_NAME = "{}_pg_{}.pdf"

def main():

    input_path = askopenfilename()
    in_file_name = os.path.basename(input_path)
    in_file_name = in_file_name[0: len(in_file_name) - len(WIN_PDF_EXTENSION)]
    
    if not input_path.endswith(WIN_PDF_EXTENSION):
        raise Exception("Invalid input file -- must be a .pdf")
    
    output_folder_path = askdirectory()

    try:
        input_file = PdfFileReader(input_path)

        for page in range(input_file.getNumPages()):
            writer = PdfFileWriter()
            writer.addPage(input_file.getPage(page))
            f_out_name = GENERIC_NAME.format(in_file_name, page + 1)

            with open(os.path.join(output_folder_path, f_out_name), 'wb') as out:
                writer.write(out)

    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()