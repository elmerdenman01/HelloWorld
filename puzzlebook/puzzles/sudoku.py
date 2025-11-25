"""
Sudoku puzzle generator
"""
import random
from typing import Dict, Any
from ..puzzle_base import Puzzle, PuzzleRegistry


@PuzzleRegistry.register
class SudokuPuzzle(Puzzle):
    """Sudoku puzzle generator"""
    
    @property
    def puzzle_type(self) -> str:
        return "Sudoku"
    
    def _is_valid_placement(self, grid, row, col, num):
        """Check if placing num at grid[row][col] is valid"""
        # Check row
        if num in grid[row]:
            return False
        
        # Check column
        if num in [grid[i][col] for i in range(9)]:
            return False
        
        # Check 3x3 box
        box_row, box_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(box_row, box_row + 3):
            for j in range(box_col, box_col + 3):
                if grid[i][j] == num:
                    return False
        
        return True
    
    def generate(self) -> Dict[str, Any]:
        """Generate a Sudoku puzzle"""
        # Create a simple 9x9 grid with some numbers filled in
        # This implementation ensures valid Sudoku rules
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
        attempts = 0
        max_attempts = cells_to_fill * 100  # Prevent infinite loops
        
        while filled < cells_to_fill and attempts < max_attempts:
            row = random.randint(0, 8)
            col = random.randint(0, 8)
            num = random.randint(1, 9)
            
            if grid[row][col] == 0 and self._is_valid_placement(grid, row, col, num):
                grid[row][col] = num
                filled += 1
            
            attempts += 1
        
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
