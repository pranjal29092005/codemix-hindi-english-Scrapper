# YouTube Comment Extractor - AI Agent Instructions

## Project Overview
Single-file Jupyter Notebook application that extracts YouTube comments from videos, playlists, and channels using the YouTube Data API v3. Outputs results to CSV files with naming pattern `comments_{video_id}.csv`.

## Architecture & Data Flow

### Core Processing Pipeline
1. **Input**: Text file containing YouTube URLs (videos, playlists, or channels)
2. **URL Detection**: Regex-based pattern matching identifies URL type in `process_link()`
3. **ID Extraction**: Three dedicated extractors (`extract_video_id()`, `extract_playlist_id()`, `extract_channel_id()`)
4. **Video Resolution**: Playlists/channels → video IDs list → individual comment fetching
5. **Output**: One CSV per video (`comments_{video_id}.csv`)

### URL Type Handling Pattern
- **Playlists**: Extract `list=` parameter → fetch all video IDs (paginated, 50/page)
- **Channels**: Support both `/channel/{id}` and `/@{username}` formats → get uploads playlist → fetch video IDs
- **Videos**: Direct extraction from various URL formats (watch?v=, youtu.be/, /shorts/, /embed/)

## Critical Configuration

### API Key Management
- Set `API_KEY` variable in the main code cell before execution
- **Quota Awareness**: Daily limit is 10,000 units (see [quota costs](https://developers.google.com/youtube/v3/determine_quota_cost))
- Typical costs: `commentThreads.list` = 1 unit, `playlistItems.list` = 1 unit
- For high-volume usage, implement API key rotation (mentioned in notebook but not implemented)

### Input File Path
- Default: `/content/Test.txt` (Google Colab path)
- **Local Windows usage**: Update `filename` in `main()` to Windows path (e.g., `C:\\YOUTUBESCRAPPER\\urls.txt`)
- Format: One URL per line, empty lines ignored

## Development Workflow

### Running the Notebook
1. Execute cell 1 (markdown documentation) - informational only
2. Execute cell 2: `!pip install google-api-python-client` - installs dependency
3. Update `API_KEY` variable in cell 3
4. Update `filename` path in cell 3 if not using Colab default
5. Execute cell 3 - runs entire extraction process

### Pagination Pattern
All API calls use consistent pagination:
```python
next_page_token = None
while True:
    request = youtube.{method}().list(..., pageToken=next_page_token)
    response = request.execute()
    # process items
    next_page_token = response.get("nextPageToken")
    if not next_page_token:
        break
```
Always use `maxResults=50` for playlist items (API maximum), `maxResults=100` for comments.

### Output Convention
- CSV files written to current working directory
- Single column: "Comment" header
- Filename: `comments_{11-char-video-id}.csv`
- Encoding: UTF-8 with newline="" for cross-platform compatibility

## Project-Specific Patterns

### Regex ID Extraction
Video IDs are 11 alphanumeric characters matched across multiple URL formats:
```python
r"(?:v=|\/embed\/|\/\d+\/|\/vi?\/|watch\?v=|youtu\.be\/|\/v\/|\/shorts\/)([a-zA-Z0-9_-]{11})"
```

### Channel ID Resolution
Modern YouTube uses `/@username` format requiring API lookup via `search().list()`, while legacy `/channel/{id}` format uses direct regex extraction.

### Global API_KEY Pattern
`API_KEY` is defined as module-level constant, passed explicitly to functions requiring it rather than using environment variables or config files.

## Performance Characteristics
- **Benchmark**: ~12 seconds for 10 videos on Google Colab CPU
- **Rate limiting**: Not implemented - relies on API quota enforcement
- **Memory**: Comments accumulated in-memory before CSV write (potential issue for videos with 100K+ comments)

## Dependencies
- `google-api-python-client`: YouTube API client library
- Built-in: `csv`, `re`
- No test framework, linting, or type hints currently used
