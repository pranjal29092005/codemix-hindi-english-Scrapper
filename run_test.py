import json

# Load notebook and execute main code cell
with open('YTCommentExtractor.ipynb', 'r', encoding='utf-8') as f:
    nb = json.load(f)

# Find the main code cell (contains API_KEY)
for cell in nb['cells']:
    if cell.get('cell_type') == 'code' and 'API_KEY' in ''.join(cell.get('source', [])):
        code = '\n'.join(cell['source'])
        exec(code)
        break
