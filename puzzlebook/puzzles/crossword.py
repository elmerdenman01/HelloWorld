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
        # Simplified crossword with clues
        # In a real implementation, this would use a dictionary and placement algorithm
        
        clues = {
            "easy": {
                "across": {
                    "1": ("Feline pet", "CAT"),
                    "4": ("Man's best friend", "DOG"),
                    "6": ("Yellow fruit", "BANANA")
                },
                "down": {
                    "1": ("Large feline", "LION"),
                    "2": ("Flying mammal", "BAT"),
                    "5": ("Buzzing insect", "BEE")
                }
            },
            "medium": {
                "across": {
                    "1": ("Device for computing", "COMPUTER"),
                    "8": ("Written composition", "ESSAY"),
                    "10": ("Frozen water", "ICE")
                },
                "down": {
                    "1": ("Baked dessert", "CAKE"),
                    "2": ("Ocean", "SEA"),
                    "5": ("Vehicle", "CAR")
                }
            },
            "hard": {
                "across": {
                    "1": ("Study of ancient life", "PALEONTOLOGY"),
                    "7": ("Relating to astronomy", "CELESTIAL"),
                    "12": ("Complex", "INTRICATE")
                },
                "down": {
                    "1": ("Musical instrument", "PIANO"),
                    "3": ("Scientific procedure", "EXPERIMENT"),
                    "8": ("Achievement", "SUCCESS")
                }
            }
        }
        
        puzzle_clues = clues.get(self.difficulty, clues["medium"])
        
        return {
            'clues': puzzle_clues,
            'difficulty': self.difficulty
        }
    
    def to_html(self) -> str:
        """Convert Crossword puzzle to HTML"""
        data = self.generate()
        clues = data['clues']
        
        html = '<div class="puzzle crossword">\n'
        html += f'<h3>Crossword ({self.difficulty.capitalize()})</h3>\n'
        
        # Across clues
        html += '<div class="clues">\n'
        html += '<div class="across-clues">\n'
        html += '<h4>Across</h4>\n'
        html += '<ol>\n'
        for num, (clue, _) in sorted(clues['across'].items()):
            html += f'<li value="{num}">{clue}</li>\n'
        html += '</ol>\n'
        html += '</div>\n'
        
        # Down clues
        html += '<div class="down-clues">\n'
        html += '<h4>Down</h4>\n'
        html += '<ol>\n'
        for num, (clue, _) in sorted(clues['down'].items()):
            html += f'<li value="{num}">{clue}</li>\n'
        html += '</ol>\n'
        html += '</div>\n'
        html += '</div>\n'
        
        html += '<div class="crossword-grid">\n'
        html += '<p><em>[Grid for puzzle - fill in the answers based on clues above]</em></p>\n'
        html += '</div>\n'
        
        html += '</div>\n'
        
        return html
