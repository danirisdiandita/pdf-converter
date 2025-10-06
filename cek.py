
import json 

error_lang = ["am", "ar", "bn", "fa", "he", "hi", "hy", 
"ka", "km", "kn", "lo", "ml", "mr", "my", 
"ne", "si", "ta", "te", "th", "ur", "yi"]

langs = []
with open('lang.json') as f: 
    langs = json.load(f)

for lang in langs:
    if lang['key'] in error_lang:
        print(lang)
