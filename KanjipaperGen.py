import markdown
from bottle import TEMPLATE_PATH, jinja2_template as template
import pdfkit
import sys
import os
import argparse

class KanjipaperGen:
    def __init__(self):
        self.BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        # テンプレートファイルを設置するディレクトリのパスを指定
        TEMPLATE_PATH.append(self.BASE_DIR + "/templetes")
        self.md = markdown.Markdown()
        self.html = ''

    def GenMDtpl(self):
        sample = '## Q1.\nA.  B.  C.  D. \n## Q2. \nA.  B.  C.  D. \n## Q3.\nA.  B.  C.  D.\n## Q4.\nA.  B.  C.  D.\n## Q5.　\nA.  B.  C.  D.'

        with open('templete.md',mode='w') as f:
            f.write(sample)

    def ConvMDtoHTML(self,file):
        with open(file,mode='r') as f:
            doc = f.readlines()

        md = ''.join(doc)
        body = self.md.convert(md)
        self.html = template('base',c=body)

    def GenPDF(self,file):
        options = {
             'page-size': 'A4',
             'margin-top': '0.75in',
             'margin-right': '0.75in',
             'margin-bottom': '0.75in',
             'margin-left': '0.75in',
             'encoding': "UTF-8"
         }
        pdfkit.from_string(self.html, file, options=options)

def ConvMDtoPDF(args):
    kpg = KanjipaperGen()
    kpg.ConvMDtoHTML(args.input)
    kpg.GenPDF(args.output)

def GenMDtpl(args):
    kpg = KanjipaperGen()
    kpg.GenMDtpl()

def main():

    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers()

    init_parser = subparsers.add_parser('init')
    init_parser.set_defaults(func=GenMDtpl)

    conv_parser = subparsers.add_parser('conv')
    conv_parser.add_argument('-i', '--input',default='templete.md')
    conv_parser.add_argument('-o', '--output',default='out.pdf')
    conv_parser.set_defaults(func=ConvMDtoPDF)

    args = parser.parse_args()
    args.func(args)

if __name__ == '__main__':
    main()
