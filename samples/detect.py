text = ''
import json 
import re 
import subprocess 
with open('/data/chars/bn.json') as json_file:
    data = json.load(json_file)

bengali_set = set(data)

with open('/data/outputs/mixed_bengali.md') as f: 
    text = f.read()

# preprocessed_text = ''

pattern = r'([\u0980-\u09FF]+)'
wrapped = re.sub(pattern, r'\\textbengali{\1}', text)
print(wrapped)

md_outpath = '/data/outputs/preprocessed_bengali.md'
pdf_outpath = '/data/outputs/preprocessed_bengali.pdf'

with open(md_outpath, 'w') as f: 
    f.write(wrapped)

result = subprocess.run([
                    "pandoc", 
                    "--pdf-engine=xelatex",
                    "--include-in-header=/data/header.tex",
                    '-V geometry:"top=1.2cm, bottom=1.2cm, left=1.2cm, right=1.2cm"', 
                    md_outpath, 
                    "-o", 
                    pdf_outpath
                ], capture_output=True, text=True) # -V geometry:margin=1in





