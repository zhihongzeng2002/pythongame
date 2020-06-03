# 1/23/2020 Zhihong Zeng
# 

import argparse
import os, io
import json
import re
from PyPDF2 import PdfFileReader, PdfFileWriter, PdfFileMerger
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter


def single_merge(src_dir, des_file):
    file_list = [x for x in os.listdir(src_dir) if os.path.splitext(x)[-1] == '.pdf']
    file_list.sort(key=lambda x: x[0])
    print(file_list)

    merger = PdfFileMerger(strict=False)
    pdf_page =[]
    for f in file_list:
        file_path = os.path.join(src_dir, f)
        fh = PdfFileReader(open(file_path, 'rb'))
        merger.append(fh)
        pdf_page.append((f, fh.getNumPages())) 
    # print(pdf_page)
    text = 'Contents'
    page = 2
    for item in pdf_page:
        text += '\n{}: {}'.format(item[0], page)
        page += item[1]
    merger.merge(0, add_cover(text))

    merger.write(open(des_file, 'wb'))


def add_cover(cover_text):
    packet = io.BytesIO()
    can = canvas.Canvas(packet, pagesize=letter)

    textObj = can.beginText()
    textObj.setTextOrigin(50, 700)
    textObj.textLines(cover_text)

    can.drawText(textObj)
    can.save()

    packet.seek(0)
    return PdfFileReader(packet)

def parse():
    parser = argparse.ArgumentParser()
    parser.add_argument('--src_dir', help='source pdfs directory', required=True)
    parser.add_argument('--des_file', help='destination file path', required=True)
    args = parser.parse_args()
    return args


if __name__ == '__main__':
    args = parse()
    single_merge(args.src_dir, args.des_file)