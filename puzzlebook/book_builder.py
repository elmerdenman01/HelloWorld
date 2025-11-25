"""
Puzzle Book Builder
Compiles selected puzzles into a Kindle-compatible book format
"""
from typing import List, Dict
from datetime import datetime
from .puzzle_base import PuzzleRegistry

# Import all puzzle types to register them
from .puzzles.sudoku import SudokuPuzzle
from .puzzles.wordsearch import WordSearchPuzzle
from .puzzles.crossword import CrosswordPuzzle
from .puzzles.maze import MazePuzzle


class PuzzleBookBuilder:
    """Build a puzzle book from selected puzzle types"""
    
    def __init__(self, title: str = "My Puzzle Book"):
        self.title = title
        self.puzzles = []
        self.author = "Puzzle Book Generator"
        
    def add_puzzles(self, puzzle_type: str, count: int = 5, difficulty: str = "medium"):
        """Add puzzles of a specific type to the book"""
        for _ in range(count):
            puzzle = PuzzleRegistry.create_puzzle(puzzle_type, difficulty)
            self.puzzles.append(puzzle)
    
    def build_html(self) -> str:
        """Build the complete HTML book"""
        html = self._get_html_header()
        
        # Add cover/title page
        html += '<div class="title-page">\n'
        html += f'<h1>{self.title}</h1>\n'
        html += f'<p class="author">by {self.author}</p>\n'
        html += f'<p class="date">{datetime.now().strftime("%Y")}</p>\n'
        html += '</div>\n'
        
        # Add table of contents
        html += '<div class="toc">\n'
        html += '<h2>Contents</h2>\n'
        html += '<ul>\n'
        
        puzzle_counts = {}
        for puzzle in self.puzzles:
            puzzle_type = puzzle.puzzle_type
            puzzle_counts[puzzle_type] = puzzle_counts.get(puzzle_type, 0) + 1
        
        for puzzle_type, count in puzzle_counts.items():
            html += f'<li>{puzzle_type} Puzzles ({count})</li>\n'
        html += '</ul>\n'
        html += '</div>\n'
        
        # Add each puzzle
        for i, puzzle in enumerate(self.puzzles, 1):
            html += f'<div class="puzzle-page" id="puzzle-{i}">\n'
            html += f'<div class="puzzle-number">Puzzle #{i}</div>\n'
            html += puzzle.to_html()
            html += '</div>\n'
            html += '<div class="page-break"></div>\n'
        
        html += self._get_html_footer()
        
        return html
    
    def save_to_file(self, filename: str = None):
        """Save the puzzle book to an HTML file"""
        if filename is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"puzzlebook_{timestamp}.html"
        
        html = self.build_html()
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(html)
        
        return filename
    
    def _get_html_header(self) -> str:
        """Get HTML header with CSS styling"""
        return '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>''' + self.title + '''</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
            line-height: 1.6;
        }
        
        .title-page {
            text-align: center;
            margin: 100px 0;
        }
        
        .title-page h1 {
            font-size: 2.5em;
            margin-bottom: 20px;
        }
        
        .author {
            font-size: 1.2em;
            font-style: italic;
        }
        
        .toc {
            margin: 50px 0;
        }
        
        .toc h2 {
            border-bottom: 2px solid #333;
            padding-bottom: 10px;
        }
        
        .toc ul {
            list-style-type: none;
            padding-left: 20px;
        }
        
        .toc li {
            margin: 10px 0;
            font-size: 1.1em;
        }
        
        .puzzle-page {
            margin: 30px 0;
        }
        
        .puzzle-number {
            font-size: 1.2em;
            font-weight: bold;
            margin-bottom: 10px;
            color: #555;
        }
        
        .puzzle {
            margin: 20px 0;
            page-break-inside: avoid;
        }
        
        .puzzle h3 {
            font-size: 1.5em;
            margin-bottom: 15px;
            border-bottom: 1px solid #ddd;
            padding-bottom: 5px;
        }
        
        /* Sudoku styles */
        .sudoku-grid {
            border-collapse: collapse;
            margin: 20px auto;
            font-size: 18px;
        }
        
        .sudoku-cell {
            width: 35px;
            height: 35px;
            border: 1px solid #999;
            text-align: center;
            font-weight: bold;
        }
        
        .sudoku-cell.border-top {
            border-top: 2px solid #000;
        }
        
        .sudoku-cell.border-left {
            border-left: 2px solid #000;
        }
        
        /* Word Search styles */
        .word-search-grid {
            border-collapse: collapse;
            margin: 20px auto;
            font-size: 14px;
        }
        
        .ws-cell {
            width: 25px;
            height: 25px;
            border: 1px solid #ccc;
            text-align: center;
            font-family: monospace;
        }
        
        .word-list {
            margin: 15px 0;
            padding: 10px;
            background-color: #f5f5f5;
            border-radius: 5px;
        }
        
        /* Crossword styles */
        .clues {
            margin: 20px 0;
        }
        
        .across-clues, .down-clues {
            margin: 15px 0;
        }
        
        .clues h4 {
            font-size: 1.2em;
            margin-bottom: 10px;
        }
        
        .clues ol {
            padding-left: 30px;
        }
        
        .clues li {
            margin: 8px 0;
        }
        
        .crossword-grid {
            margin: 20px 0;
            padding: 15px;
            background-color: #f9f9f9;
            border: 1px solid #ddd;
        }
        
        .crossword-table {
            border-collapse: collapse;
            margin: 20px auto;
        }
        
        .crossword-cell {
            width: 30px;
            height: 30px;
            border: 1px solid #333;
            text-align: center;
            vertical-align: top;
            position: relative;
            padding: 2px;
        }
        
        .crossword-cell.white-cell {
            background-color: #fff;
        }
        
        .crossword-cell.black-cell {
            background-color: #000;
            border: 1px solid #000;
        }
        
        .cell-number {
            position: absolute;
            top: 2px;
            left: 3px;
            font-size: 8px;
            font-weight: bold;
        }
        
        /* Maze styles */
        .maze-grid {
            border-collapse: collapse;
            margin: 20px auto;
        }
        
        .maze-cell {
            width: 20px;
            height: 20px;
            border: 1px solid #ddd;
            text-align: center;
            font-size: 10px;
            font-weight: bold;
        }
        
        .maze-cell.wall {
            background-color: #333;
        }
        
        .maze-cell.path {
            background-color: #fff;
        }
        
        .page-break {
            page-break-after: always;
        }
        
        @media print {
            .page-break {
                page-break-after: always;
            }
        }
    </style>
</head>
<body>
'''
    
    def _get_html_footer(self) -> str:
        """Get HTML footer"""
        return '''
</body>
</html>
'''
    
    @staticmethod
    def get_available_puzzle_types() -> List[str]:
        """Get list of available puzzle types"""
        return PuzzleRegistry.get_available_puzzles()
