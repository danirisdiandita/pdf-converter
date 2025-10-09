import subprocess 
import os 
import json
import time

for file_ in os.listdir("/data/inputs"):
    fpath = os.path.join("/data/inputs", file_)

    content = [] 
    with open(fpath, "r") as f:
        content = json.load(f)

    for item in content: 
        start_wrapper = ''
        end_wrapper = ''

        if item['lang'] == 'am': 
            start_wrapper = '\\begin{amharic}\n'
            end_wrapper = '\\end{amharic}\n'
        elif item['lang'] == 'ar': 
            start_wrapper = '\\begin{arabic}\n'
            end_wrapper = '\\end{arabic}\n'
        elif item['lang'] == 'bn': 
            start_wrapper = '\\begin{bengali}\n'
            end_wrapper = '\\end{bengali}\n'
        elif item['lang'] == 'fa': 
            start_wrapper = '\\begin{persian}\n'
            end_wrapper = '\\end{persian}\n'
        elif item['lang'] == 'he': 
            start_wrapper = '\\begin{hebrew}\n'
            end_wrapper = '\\end{hebrew}\n'
        elif item['lang'] == 'hi': 
            start_wrapper = '\\begin{hindi}\n'
            end_wrapper = '\\end{hindi}\n'
        elif item['lang'] == 'hy': 
            start_wrapper = '\\begin{armenian}\n'
            end_wrapper = '\\end{armenian}\n'
        elif item['lang'] == 'ka': 
            start_wrapper = '\\begin{georgian}\n'
            end_wrapper = '\\end{georgian}\n'
        elif item['lang'] == 'km': 
            start_wrapper = '\\begin{khmer}\n'
            end_wrapper = '\\end{khmer}\n'
        elif item['lang'] == 'kn': 
            start_wrapper = '\\begin{kannada}\n'
            end_wrapper = '\\end{kannada}\n'
        elif item['lang'] == 'lo': 
            start_wrapper = '\\begin{lao}\n'
            end_wrapper = '\\end{lao}\n'
        elif item['lang'] == 'ml': 
            start_wrapper = '\\begin{malayalam}\n'
            end_wrapper = '\\end{malayalam}\n'
        elif item['lang'] == 'mr': 
            start_wrapper = '\\begin{marathi}\n'
            end_wrapper = '\\end{marathi}\n'
        elif item['lang'] == 'my': 
            start_wrapper = '\\begin{myanmar}\n'
            end_wrapper = '\\end{myanmar}\n'
        elif item['lang'] == 'ne': 
            start_wrapper = '\\begin{nepali}\n'
            end_wrapper = '\\end{nepali}\n'
        elif item['lang'] == 'si': 
            start_wrapper = '\\begin{sinhala}\n'
            end_wrapper = '\\end{sinhala}\n'
        elif item['lang'] == 'ta': 
            start_wrapper = '\\begin{tamil}\n'
            end_wrapper = '\\end{tamil}\n'
        elif item['lang'] == 'te': 
            start_wrapper = '\\begin{telugu}\n'
            end_wrapper = '\\end{telugu}\n'
        elif item['lang'] == 'th': 
            start_wrapper = '\\begin{thai}\n'
            end_wrapper = '\\end{thai}\n'
        elif item['lang'] == 'ur': 
            start_wrapper = '\\begin{urdu}\n'
            end_wrapper = '\\end{urdu}\n'
        elif item['lang'] == 'yi': 
            start_wrapper = '\\begin{yiddish}\n'
            end_wrapper = '\\end{yiddish}\n'

        if item['lang'] in [
                "am",
                "ar",
                "bn",
                "fa",
                "he",
                "hi",
                "hy",
                "ka",
                "km",
                "kn",
                "lo",
                "ml",
                "mr",
                "my",
                "ne",
                "si",
                "ta",
                "te",
                "th",
                "ur",
                "yi"
                ]: 
        
            try: 
                start_time = time.time()
                # save to md 
                md_path = os.path.join("/data/outputs", item['lang'] + ".md")
                with open(md_path, "w") as md_f: 
                    md_f.write(start_wrapper)
                    md_f.write(item['text'])
                    md_f.write(end_wrapper)

                # Convert to PDF using universal font configuration from header.tex
                # No need to specify fonts per language - XeLaTeX handles it automatically
                pdf_path = os.path.join("/data/outputs", item['lang'] + ".pdf")
                result = subprocess.run([
                    "pandoc", 
                    "--pdf-engine=xelatex",
                    "--include-in-header=/data/header.tex",
                    md_path, 
                    "-o", 
                    pdf_path
                ], capture_output=True, text=True)

                end_time = time.time() 

                print('time taken', end_time - start_time)

                # Check if pandoc command succeeded
                if result.returncode != 0:
                    raise Exception(f"Pandoc failed with code {result.returncode}: {result.stderr}")
                
                # Small delay to ensure file is written
                time.sleep(0.1)
                
                if os.path.exists(pdf_path) == False: 
                    error_msg = f"PDF not created. Pandoc stderr: {result.stderr}"
                    raise Exception(error_msg)
            except Exception as e: 
                with open("/data/outputs/error.log", "a") as f: 
                    f.write(file_ + "\t" + item['lang'] + "\t" + str(e) + "\n")

        

    # docker exec pdf-converter pandoc /data/outputs/gitu.md -o /data/outputs/gitu.pdf