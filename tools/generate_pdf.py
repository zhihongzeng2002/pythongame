# Zhihong Zeng
# 5/11/2020

import argparse
import img2pdf
from PIL import Image

def main(src_file, des_file):
    flist = src_file.split(',')
    print(flist)

    with open(des_file, 'w+b') as fh:
            fh.write(img2pdf.convert(flist))
    print('The job is done')


def parse():
    parser = argparse.ArgumentParser()
    parser.add_argument('--src_file', help='source image file', required=True)
    parser.add_argument('--des_file', help='destination pdf file', required=True)

    return parser.parse_args()

if __name__ == '__main__':
    args = parse()
    main(args.src_file, args.des_file)

