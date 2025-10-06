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
        if item['lang'] == 'bn': 
            try: 
                # save to md 
                md_path = os.path.join("/data/outputs", item['lang'] + ".md")
                with open(md_path, "w") as md_f: 
                    md_f.write(item['text'])

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