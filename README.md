# Puzzle Book Generator

An application that builds custom puzzle books for Amazon Kindle publishing. Users can select from multiple puzzle types and generate a professional-looking puzzle book in HTML format, ready to be converted for Kindle.

## Features

- **Multiple Puzzle Types**: Sudoku, Word Search, Crossword, and Maze puzzles
- **Difficulty Levels**: Easy, Medium, and Hard for each puzzle type
- **Customizable**: Choose which puzzles to include and how many of each
- **Kindle-Ready**: Generates HTML format optimized for e-reader display
- **Professional Layout**: Clean, print-friendly design with table of contents
- **Easy to Use**: Interactive CLI interface for puzzle selection

## Available Puzzle Types

1. **Sudoku** - Classic 9x9 number placement puzzles
2. **Word Search** - Find hidden words in letter grids
3. **Crossword** - Traditional crossword puzzles with clues
4. **Maze** - Navigate from start to end through maze paths

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/elmerdenman01/HelloWorld.git
   cd HelloWorld
   ```

2. No external dependencies required - uses Python standard library only!

## Usage

### Interactive Mode

Run the interactive CLI to create a custom puzzle book:

```bash
python generate_book.py
```

Follow the prompts to:
1. Select puzzle types from the menu
2. Enter a book title
3. Choose difficulty level
4. Specify number of puzzles per type

### Quick Demo

Generate a sample puzzle book with predefined settings:

```bash
python demo.py
```

This creates `demo_puzzlebook.html` with a mix of all puzzle types.

### Programmatic Usage

Create puzzle books programmatically in Python:

```python
from puzzlebook.book_builder import PuzzleBookBuilder

# Create a new book
builder = PuzzleBookBuilder(title="My Custom Puzzle Book")

# Add puzzles
builder.add_puzzles("Sudoku", count=5, difficulty="medium")
builder.add_puzzles("Word Search", count=3, difficulty="easy")
builder.add_puzzles("Maze", count=4, difficulty="hard")

# Save to file
filename = builder.save_to_file()
print(f"Book created: {filename}")
```

## Publishing to Amazon Kindle

1. **Generate your puzzle book** using this tool (creates HTML file)
2. **Convert to Kindle format**:
   - Open the HTML file in a web browser
   - Print to PDF (recommended for best quality)
   - Use Amazon's Kindle Create tool or Calibre to convert to MOBI/KPF format
3. **Upload to KDP** (Kindle Direct Publishing)
   - Go to kdp.amazon.com
   - Create a new title
   - Upload your converted puzzle book
   - Set pricing and publish

## Project Structure

```
HelloWorld/
├── puzzlebook/           # Main package
│   ├── __init__.py
│   ├── puzzle_base.py    # Base classes and registry
│   ├── book_builder.py   # Book compilation
│   └── puzzles/          # Puzzle implementations
│       ├── __init__.py
│       ├── sudoku.py
│       ├── wordsearch.py
│       ├── crossword.py
│       └── maze.py
├── tests/                # Unit tests
│   ├── test_puzzles.py
│   └── test_book_builder.py
├── generate_book.py      # Interactive CLI
├── demo.py              # Demo script
└── README.md            # This file
```

## Running Tests

Execute the test suite:

```bash
python -m unittest discover tests
```

Run specific test modules:

```bash
python -m unittest tests.test_puzzles
python -m unittest tests.test_book_builder
```

## Extending the Application

### Adding New Puzzle Types

1. Create a new puzzle class in `puzzlebook/puzzles/`
2. Inherit from `Puzzle` base class
3. Implement required methods: `generate()`, `to_html()`, `puzzle_type`
4. Decorate with `@PuzzleRegistry.register`
5. Import in `book_builder.py`

Example:

```python
from ..puzzle_base import Puzzle, PuzzleRegistry

@PuzzleRegistry.register
class MyPuzzle(Puzzle):
    @property
    def puzzle_type(self) -> str:
        return "My Puzzle Type"
    
    def generate(self) -> Dict[str, Any]:
        # Generate puzzle data
        return {'data': 'puzzle_data'}
    
    def to_html(self) -> str:
        # Return HTML representation
        return '<div class="puzzle">...</div>'
```

## License

MIT License - Feel free to use and modify for your puzzle book projects!

## Contributing

Contributions are welcome! Feel free to submit pull requests or open issues.

## Support

For questions or issues, please open an issue on GitHub.
