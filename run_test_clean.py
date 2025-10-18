import os
import time

# Close and rename old file
old_file = 'hinglish_comments_all.csv'
if os.path.exists(old_file):
    try:
        os.rename(old_file, 'hinglish_comments_all_old.csv')
        print("Renamed old CSV file")
    except:
        print("Could not rename - file may be open. Waiting...")
        time.sleep(2)

# Now run the main extraction
import json

with open('YTCommentExtractor.ipynb', 'r', encoding='utf-8') as f:
    nb = json.load(f)

for cell in nb['cells']:
    if cell.get('cell_type') == 'code' and 'API_KEY' in ''.join(cell.get('source', [])):
        code = '\n'.join(cell['source'])
        exec(code)
        break
