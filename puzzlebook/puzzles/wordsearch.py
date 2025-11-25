"""
Word Search puzzle generator
"""
import random
import string
from typing import Dict, Any, List
from ..puzzle_base import Puzzle, PuzzleRegistry


@PuzzleRegistry.register
class WordSearchPuzzle(Puzzle):
    """Word Search puzzle generator"""
    
    @property
    def puzzle_type(self) -> str:
        return "Word Search"
    
    def generate(self) -> Dict[str, Any]:
        """Generate a Word Search puzzle"""
        # Sample word lists by difficulty
        word_lists = {
            "easy": ["CAT", "DOG", "BIRD", "FISH", "BEAR", "LION", "FROG", "DUCK"],
            "medium": ["APPLE", "ORANGE", "BANANA", "GRAPE", "MELON", "PEACH", "LEMON", "BERRY"],
            "hard": ["COMPUTER", "KEYBOARD", "DISPLAY", "PRINTER", "SCANNER", "NETWORK", "SOFTWARE"]
        }
        
        words = word_lists.get(self.difficulty, word_lists["medium"])
        grid_size = 12 if self.difficulty == "easy" else 15
        
        # Create empty grid
        grid = [['' for _ in range(grid_size)] for _ in range(grid_size)]
        
        # Place words in the grid
        placed_words = []
        for word in words[:6]:  # Limit to 6 words for simplicity
            # Try to place word horizontally or vertically
            direction = random.choice(['horizontal', 'vertical'])
            placed = False
            attempts = 0
            
            while not placed and attempts < 50:
                if direction == 'horizontal':
                    row = random.randint(0, grid_size - 1)
                    col = random.randint(0, grid_size - len(word))
                    if all(grid[row][col + i] == '' for i in range(len(word))):
                        for i, char in enumerate(word):
                            grid[row][col + i] = char
                        placed = True
                        placed_words.append(word)
                else:  # vertical
                    row = random.randint(0, grid_size - len(word))
                    col = random.randint(0, grid_size - 1)
                    if all(grid[row + i][col] == '' for i in range(len(word))):
                        for i, char in enumerate(word):
                            grid[row + i][col] = char
                        placed = True
                        placed_words.append(word)
                attempts += 1
        
        # Fill empty cells with random letters
        for i in range(grid_size):
            for j in range(grid_size):
                if grid[i][j] == '':
                    grid[i][j] = random.choice(string.ascii_uppercase)
        
        return {
            'grid': grid,
            'words': placed_words,
            'difficulty': self.difficulty
        }
    
    def to_html(self) -> str:
        """Convert Word Search puzzle to HTML"""
        data = self.generate()
        grid = data['grid']
        words = data['words']
        
        html = '<div class="puzzle word-search">\n'
        html += f'<h3>Word Search ({self.difficulty.capitalize()})</h3>\n'
        html += '<div class="word-list"><strong>Find these words:</strong> '
        html += ', '.join(words)
        html += '</div>\n'
        html += '<table class="word-search-grid">\n'
        
        for row in grid:
            html += '<tr>\n'
            for cell in row:
                html += f'<td class="ws-cell">{cell}</td>\n'
            html += '</tr>\n'
        
        html += '</table>\n'
        html += '</div>\n'
        
        return html
