"""
Maze puzzle generator
"""
import random
from typing import Dict, Any, List, Tuple
from ..puzzle_base import Puzzle, PuzzleRegistry


@PuzzleRegistry.register
class MazePuzzle(Puzzle):
    """Maze puzzle generator"""
    
    @property
    def puzzle_type(self) -> str:
        return "Maze"
    
    def generate(self) -> Dict[str, Any]:
        """Generate a Maze puzzle"""
        # Determine maze size based on difficulty
        if self.difficulty == "easy":
            size = 10
        elif self.difficulty == "hard":
            size = 20
        else:  # medium
            size = 15
        
        # Create a simple maze using recursive backtracking algorithm (simplified)
        maze = [[1 for _ in range(size)] for _ in range(size)]  # 1 = wall, 0 = path
        
        # Create a simple path from start to end
        # Start at top-left, end at bottom-right
        current_row, current_col = 0, 0
        maze[current_row][current_col] = 0  # Start
        
        # Create random path to the end
        while current_row < size - 1 or current_col < size - 1:
            maze[current_row][current_col] = 0
            
            # Randomly choose to move right or down (with some randomness for branches)
            possible_moves = []
            if current_row < size - 1:
                possible_moves.append(('down', current_row + 1, current_col))
            if current_col < size - 1:
                possible_moves.append(('right', current_row, current_col + 1))
            
            if possible_moves:
                direction, current_row, current_col = random.choice(possible_moves)
        
        maze[current_row][current_col] = 0  # End
        
        # Add some random paths for complexity
        for _ in range(size * 2):
            row = random.randint(0, size - 1)
            col = random.randint(0, size - 1)
            maze[row][col] = 0
        
        return {
            'maze': maze,
            'size': size,
            'start': (0, 0),
            'end': (size - 1, size - 1),
            'difficulty': self.difficulty
        }
    
    def to_html(self) -> str:
        """Convert Maze puzzle to HTML"""
        data = self.generate()
        maze = data['maze']
        size = data['size']
        
        html = '<div class="puzzle maze">\n'
        html += f'<h3>Maze ({self.difficulty.capitalize()})</h3>\n'
        html += '<p>Find the path from START (top-left) to END (bottom-right)</p>\n'
        html += '<table class="maze-grid">\n'
        
        for i, row in enumerate(maze):
            html += '<tr>\n'
            for j, cell in enumerate(row):
                cell_class = "maze-cell"
                if cell == 1:
                    cell_class += " wall"
                else:
                    cell_class += " path"
                
                # Mark start and end
                content = ""
                if i == 0 and j == 0:
                    content = "S"
                elif i == size - 1 and j == size - 1:
                    content = "E"
                
                html += f'<td class="{cell_class}">{content}</td>\n'
            html += '</tr>\n'
        
        html += '</table>\n'
        html += '</div>\n'
        
        return html
