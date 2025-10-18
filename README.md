# Code-Mixed Hindi-English (Hinglish) Comment Scraper

A YouTube comment extraction tool that automatically identifies and collects code-mixed Hindi-English (Hinglish) comments from YouTube videos, playlists, and channels.

## Features

- ✅ **Dual Script Support**: Detects both Devanagari-English and Roman-script Hinglish
- ✅ **Smart Filtering**: Uses word-list approach with 80+ common Hinglish words
- ✅ **Clean Output**: Removes HTML tags, URLs, emojis, and special characters
- ✅ **Complete Sentences**: Ensures minimum length and quality validation
- ✅ **Bulk Processing**: Process multiple channels/playlists/videos from a file
- ✅ **CSV Export**: Individual per-video CSVs + merged result file

## Requirements

- Python 3.7+
- YouTube Data API v3 key
- `google-api-python-client`

## Installation

1. Clone the repository:
```bash
git clone https://github.com/pranjal29092005/codemix-hindi-english-Scrapper.git
cd codemix-hindi-english-Scrapper
```

2. Install dependencies:
```bash
pip install google-api-python-client
```

3. Set up your API key:
   - Create a `.env` file in the project root
   - Add your YouTube API key:
   ```
   YOUTUBE_API_KEY=your_api_key_here
   ```

## Usage

### 1. Prepare Input File

Create `urls.txt` with YouTube URLs (one per line):
```
https://youtube.com/@channelname
https://youtube.com/watch?v=VIDEO_ID
https://youtube.com/playlist?list=PLAYLIST_ID
```

### 2. Run Extraction

**Option A: Jupyter Notebook**
```bash
jupyter notebook YTCommentExtractor.ipynb
```
Run all cells to start extraction.

**Option B: Python Script**
```python
# Run the notebook cell directly
python run_test_clean.py
```

### 3. Merge Results

Combine all individual CSV files into one:
```bash
python merge_csv.py
```

Output: `result.csv` with 20,000 Hinglish comments

## How It Works

### Hinglish Detection

The tool uses two methods to identify code-mixed content:

1. **Devanagari + English**: Detects Unicode Devanagari characters mixed with ASCII English
2. **Roman Hinglish**: Uses word-list matching (15% threshold) for WhatsApp-style Hinglish

Example detected comments:
- `"Osho ki original hindi all books kha se buy kare"` (Roman Hinglish)
- `"meri kundalini ho gayi activate ab kya karu lol"` (Roman Hinglish)
- `"Osho को koti koti naman"` (Devanagari + English)

### Text Cleaning

All comments are cleaned to remove:
- HTML tags and entities (`<a>`, `&nbsp;`, etc.)
- URLs and links
- Emojis (comprehensive Unicode range removal)
- Special symbols and arrows
- Extra whitespace

### Quality Filters

- Minimum 15 characters per comment
- At least 3 words for Roman-script detection
- Complete sentence validation

## Output Format

### Individual Files
`comments_{VIDEO_ID}.csv` - One file per video

### Merged File
`result.csv` - Combined output with structure:
```csv
Comment
"first hinglish comment here"
"second hinglish comment here"
...
```

## Configuration

Edit in `YTCommentExtractor.ipynb`:

```python
COMMENT_LIMIT = 20000  # Max comments to collect
```

Update input file path (default: `C:\YOUTUBESCRAPPER\urls.txt`):
```python
filename = r"C:\YOUTUBESCRAPPER\urls.txt"
```

## API Quota

YouTube Data API v3 has a daily quota limit of **10,000 units**.

Typical costs per operation:
- `commentThreads.list`: 1 unit
- `playlistItems.list`: 1 unit
- `channels.list`: 1 unit
- `search.list`: 100 units

For 20,000 comments from ~1000 videos, expect ~1000-2000 quota units.

## Project Structure

```
├── .env                          # API key (gitignored)
├── .gitignore                    # Ignore patterns
├── YTCommentExtractor.ipynb      # Main notebook
├── urls.txt                      # Input URLs
├── merge_csv.py                  # Merge helper script
├── run_test_clean.py            # Execution helper
└── README.md                     # This file
```

## Hinglish Word List

The tool includes 80+ common Hindi words in Roman script:
- Pronouns: `hai`, `ho`, `ka`, `ki`, `ko`, `ke`
- Common words: `yaar`, `bhai`, `kya`, `kaise`, `matlab`
- Verbs: `karo`, `dekho`, `suno`, `chalo`
- Expressions: `achha`, `sahi`, `bilkul`, `waah`

## Troubleshooting

**File Lock Error**
```
PermissionError: Permission denied: 'hinglish_comments_all.csv'
```
Close the CSV file in any editor before running the script.

**API Key Not Found**
```
ValueError: API key not found
```
Ensure `.env` file exists with `YOUTUBE_API_KEY=your_key`.

**Quota Exceeded**
```
quotaExceeded: The request cannot be completed
```
Wait 24 hours for quota reset or use a different API key.

## Contributing

Contributions welcome! Areas for improvement:
- Additional language support
- Better emoji detection
- Optimized API quota usage
- Parallel processing

## License

MIT License - see LICENSE file for details.

## Acknowledgments

- YouTube Data API v3
- Google API Python Client
- Hinglish NLP research community

## Author

[@pranjal29092005](https://github.com/pranjal29092005)

---

**Note**: This tool is for research and educational purposes. Respect YouTube's Terms of Service and content creators' rights when using scraped data.
