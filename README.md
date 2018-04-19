## KanjipaperGen
markdownで記述した漢字テストをpdf出力するCLI

### How to use
- テンプレート作成
- - python KanjipaperGen.py init
- pdf生成
- - python KanjipaperGen.py conv -i [input] -o [output] -img

### Other
以下のコマンドで自作コマンド化  
pip install -e .

### install requirement
apt-get install wkhtmltopdf  
pip install markdown  
pip install pdfkit  

### other requirement
A: nihongo soumatome Kanji N4-5
M: nihongo soumatome Kanji N3
V & R: Shun Kansen master JLPT N3

A : base on Hiragana All Kanji and Frigana
M : base on Kanji All Kanji and less Frigana
V : base on Kanji All Kanji and nothing Frigana

underline : textbook and pages


Deadline : Monday night

one page per a week
