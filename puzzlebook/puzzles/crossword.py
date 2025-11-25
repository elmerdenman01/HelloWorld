"""
Crossword puzzle generator
"""
from typing import Dict, Any
from ..puzzle_base import Puzzle, PuzzleRegistry


@PuzzleRegistry.register
class CrosswordPuzzle(Puzzle):
    """Crossword puzzle generator"""
    
    @property
    def puzzle_type(self) -> str:
        return "Crossword"
    
    def generate(self) -> Dict[str, Any]:
        """Generate a Crossword puzzle"""
        # Simplified crossword with clues and grid positions
        # In a real implementation, this would use a dictionary and placement algorithm
        
        clues = {
            "easy": {
                "across": {
                    "1": ("Feline pet", "CAT", 0, 0),  # (clue, answer, row, col)
                    "4": ("Man's best friend", "DOG", 2, 0),
                    "6": ("Yellow fruit", "BANANA", 4, 1)
                },
                "down": {
                    "1": ("Large feline", "LION", 0, 0),
                    "2": ("Flying mammal", "BAT", 0, 2),
                    "5": ("Buzzing insect", "BEE", 2, 2)
                }
            },
            "medium": {
                "across": {
                    "1": ("Device for computing", "COMPUTER", 0, 0),
                    "8": ("Written composition", "ESSAY", 4, 0),
                    "10": ("Frozen water", "ICE", 6, 2)
                },
                "down": {
                    "1": ("Baked dessert", "CAKE", 0, 0),
                    "2": ("Ocean", "SEA", 0, 4),
                    "5": ("Vehicle", "CAR", 2, 2)
                }
            },
            "hard": {
                "across": {
                    "1": ("Study of ancient life", "PALEONTOLOGY", 0, 0),
                    "7": ("Relating to astronomy", "CELESTIAL", 4, 2),
                    "12": ("Complex", "INTRICATE", 8, 1)
                },
                "down": {
                    "1": ("Musical instrument", "PIANO", 0, 0),
                    "3": ("Scientific procedure", "EXPERIMENT", 0, 6),
                    "8": ("Achievement", "SUCCESS", 4, 4)
                }
            }
        }
        
        puzzle_clues = clues.get(self.difficulty, clues["medium"])
        
        return {
            'clues': puzzle_clues,
            'difficulty': self.difficulty
        }
    
    def _create_grid(self, clues):
        """Create a 2D grid for the crossword puzzle"""
        # First, determine grid size needed
        max_row = 0
        max_col = 0
        
        # Check all across and down clues to find max dimensions
        for direction in ['across', 'down']:
            for num, clue_data in clues[direction].items():
                clue_text, answer, row, col = clue_data
                if direction == 'across':
                    # For across words: need columns up to col + len(answer) - 1
                    max_col = max(max_col, col + len(answer))
                    # For across words: need rows up to row
                    max_row = max(max_row, row + 1)
                else:  # down
                    # For down words: need rows up to row + len(answer) - 1
                    max_row = max(max_row, row + len(answer))
                    # For down words: need columns up to col
                    max_col = max(max_col, col + 1)
        
        # Create grid filled with None (black squares)
        grid = [[None for _ in range(max_col)] for _ in range(max_row)]
        
        # Track which cells have clue numbers
        clue_numbers = {}
        
        # Place across words
        for num, clue_data in clues['across'].items():
            clue_text, answer, row, col = clue_data
            for i, char in enumerate(answer):
                grid[row][col + i] = ''  # Empty cell for user to fill
            # Mark the starting cell with the clue number
            if (row, col) not in clue_numbers:
                clue_numbers[(row, col)] = []
            clue_numbers[(row, col)].append(num)
        
        # Place down words
        for num, clue_data in clues['down'].items():
            clue_text, answer, row, col = clue_data
            for i, char in enumerate(answer):
                grid[row + i][col] = ''  # Empty cell for user to fill
            # Mark the starting cell with the clue number
            if (row, col) not in clue_numbers:
                clue_numbers[(row, col)] = []
            clue_numbers[(row, col)].append(num)
        
        return grid, clue_numbers
    
    def to_html(self) -> str:
        """Convert Crossword puzzle to HTML"""
        data = self.generate()
        clues = data['clues']
        
        html = '<div class="puzzle crossword">\n'
        html += f'<h3>Crossword ({self.difficulty.capitalize()})</h3>\n'
        
        # Generate the grid
        grid, clue_numbers = self._create_grid(clues)
        
        # Create the crossword grid table
        html += '<div class="crossword-grid">\n'
        html += '<table class="crossword-table">\n'
        for i, row in enumerate(grid):
            html += '<tr>\n'
            for j, cell in enumerate(row):
                if cell is None:
                    # Black square
                    html += '<td class="crossword-cell black-cell"></td>\n'
                else:
                    # White square with optional number
                    cell_num = ''
                    if (i, j) in clue_numbers:
                        # Get unique clue numbers and join them
                        unique_nums = sorted(set(clue_numbers[(i, j)]), key=lambda x: int(x))
                        cell_num = ','.join(unique_nums)
                    html += f'<td class="crossword-cell white-cell">'
                    if cell_num:
                        html += f'<span class="cell-number">{cell_num}</span>'
                    html += '</td>\n'
            html += '</tr>\n'
        html += '</table>\n'
        html += '</div>\n'
        
        # Across clues
        html += '<div class="clues">\n'
        html += '<div class="across-clues">\n'
        html += '<h4>Across</h4>\n'
        html += '<ol>\n'
        for num, clue_data in sorted(clues['across'].items()):
            clue_text = clue_data[0]
            html += f'<li value="{num}">{clue_text}</li>\n'
        html += '</ol>\n'
        html += '</div>\n'
        
        # Down clues
        html += '<div class="down-clues">\n'
        html += '<h4>Down</h4>\n'
        html += '<ol>\n'
        for num, clue_data in sorted(clues['down'].items()):
            clue_text = clue_data[0]
            html += f'<li value="{num}">{clue_text}</li>\n'
        html += '</ol>\n'
        html += '</div>\n'
        html += '</div>\n'
        
        html += '</div>\n'
        
        return html
