"""
Sudoku puzzle generator
"""
import random
from typing import Dict, Any, List
from ..puzzle_base import Puzzle, PuzzleRegistry


@PuzzleRegistry.register
class SudokuPuzzle(Puzzle):
    """Sudoku puzzle generator"""
    
    @property
    def puzzle_type(self) -> str:
        return "Sudoku"
    
    def generate(self) -> Dict[str, Any]:
        """Generate a Sudoku puzzle"""
        # Create a simple 9x9 grid with some numbers filled in
        # This is a simplified version - a real implementation would ensure valid Sudoku rules
        grid = [[0 for _ in range(9)] for _ in range(9)]
        
        # Difficulty determines how many cells to fill
        if self.difficulty == "easy":
            cells_to_fill = 40
        elif self.difficulty == "hard":
            cells_to_fill = 25
        else:  # medium
            cells_to_fill = 30
        
        # Fill random cells with valid numbers
        filled = 0
        while filled < cells_to_fill:
            row = random.randint(0, 8)
            col = random.randint(0, 8)
            if grid[row][col] == 0:
                grid[row][col] = random.randint(1, 9)
                filled += 1
        
        return {
            'grid': grid,
            'difficulty': self.difficulty
        }
    
    def to_html(self) -> str:
        """Convert Sudoku puzzle to HTML"""
        data = self.generate()
        grid = data['grid']
        
        html = '<div class="puzzle sudoku">\n'
        html += f'<h3>Sudoku ({self.difficulty.capitalize()})</h3>\n'
        html += '<table class="sudoku-grid">\n'
        
        for i, row in enumerate(grid):
            html += '<tr>\n'
            for j, cell in enumerate(row):
                cell_class = "sudoku-cell"
                if i % 3 == 0 and i > 0:
                    cell_class += " border-top"
                if j % 3 == 0 and j > 0:
                    cell_class += " border-left"
                
                value = str(cell) if cell != 0 else ""
                html += f'<td class="{cell_class}">{value}</td>\n'
            html += '</tr>\n'
        
        html += '</table>\n'
        html += '</div>\n'
        
        return html
