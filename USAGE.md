# Quick Start Guide

## Generate Your First Puzzle Book

### Option 1: Interactive Mode (Recommended)
```bash
python generate_book.py
```
Follow the prompts to:
1. Select puzzle types (enter numbers separated by commas, or 'all')
2. Enter a custom title
3. Choose difficulty (easy/medium/hard)
4. Specify how many puzzles of each type

### Option 2: Quick Demo
```bash
python demo.py
```
Creates a sample book with all puzzle types: `demo_puzzlebook.html`

### Option 3: Custom Script
```python
from puzzlebook.book_builder import PuzzleBookBuilder

builder = PuzzleBookBuilder(title="Summer Vacation Puzzles")
builder.add_puzzles("Sudoku", count=10, difficulty="easy")
builder.add_puzzles("Word Search", count=10, difficulty="medium")
builder.save_to_file("summer_puzzles.html")
```

## Publishing to Kindle

1. **Generate** your puzzle book (creates .html file)
2. **Convert** to Kindle format:
   - Open HTML in browser
   - Print to PDF (File → Print → Save as PDF)
   - Use Kindle Create or Calibre to convert to MOBI
3. **Upload** to Amazon KDP (kdp.amazon.com)

## Testing

Run all tests:
```bash
python -m unittest discover tests
```

Quick validation:
```bash
python validate.py
```

## Available Puzzles

| Type | Description | Difficulties |
|------|-------------|--------------|
| Sudoku | 9x9 number placement | Easy, Medium, Hard |
| Word Search | Find words in letter grid | Easy, Medium, Hard |
| Crossword | Clue-based word puzzles | Easy, Medium, Hard |
| Maze | Navigate from start to end | Easy, Medium, Hard |

## Tips

- **Easy difficulty**: More clues/hints, smaller grids
- **Medium difficulty**: Balanced challenge
- **Hard difficulty**: Fewer clues, larger grids
- Mix difficulty levels for variety in your book
- Recommended: 20-50 puzzles per book for good value

## Output

- Format: HTML with embedded CSS
- Kindle-compatible styling
- Professional layout with:
  - Title page
  - Table of contents
  - Numbered puzzles
  - Page breaks for printing

Enjoy creating your puzzle books!
