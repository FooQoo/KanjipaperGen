## KanjipaperGen
markdownで記述した漢字テストをpdf出力するCLI

### How to use
- テンプレート作成
- - python KanjipaperGen.py init
- pdf生成
- - python KanjipaperGen.py conv -i [input] -o [output]

### Other
以下のコマンドで自作コマンド化  
pip install -e .

### install requirement
apt-get install wkhtmltopdf  
pip install markdown  
pip install pdfkit  
