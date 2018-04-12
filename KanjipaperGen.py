import markdown
from bottle import TEMPLATE_PATH, jinja2_template as template
import pdfkit
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

    def ConvMDintoHTML(self,file):
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

def ConvMDintoPDF(args):
    kpg = KanjipaperGen()
    kpg.ConvMDintoHTML(args.input)
    kpg.GenPDF(args.output)

def GenMDtpl(args):
    kpg = KanjipaperGen()
    kpg.GenMDtpl()
    print('Generate templete')

def main():
    usage = 'Usage: python {}  [--input <file>] [--output <file>] [--help]'\
            .format(__file__)

    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers()

    init_parser = subparsers.add_parser('init',help='generate templete')
    init_parser.set_defaults(func=GenMDtpl)

    conv_parser = subparsers.add_parser('conv',help='convert Markdown into pdf')
    conv_parser.add_argument('-i', '--input', nargs='?', default='templete.md',help='input filename')
    conv_parser.add_argument('-o', '--output',nargs='?', default='out.pdf',help='output filename')
    conv_parser.set_defaults(func=ConvMDintoPDF)

    args = parser.parse_args()
    if hasattr(args, 'func'):
        args.func(args)
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
