"""
Base puzzle class and puzzle registry
"""
from abc import ABC, abstractmethod
from typing import List, Dict, Any


class Puzzle(ABC):
    """Base class for all puzzle types"""
    
    def __init__(self, difficulty: str = "medium"):
        self.difficulty = difficulty
        
    @abstractmethod
    def generate(self) -> Dict[str, Any]:
        """Generate puzzle data"""
        pass
    
    @abstractmethod
    def to_html(self) -> str:
        """Convert puzzle to HTML format for Kindle"""
        pass
    
    @property
    @abstractmethod
    def puzzle_type(self) -> str:
        """Return the type of puzzle"""
        pass


class PuzzleRegistry:
    """Registry for available puzzle types"""
    
    _puzzles: Dict[str, type] = {}
    
    @classmethod
    def register(cls, puzzle_class: type):
        """Register a puzzle type"""
        puzzle_instance = puzzle_class()
        cls._puzzles[puzzle_instance.puzzle_type] = puzzle_class
        return puzzle_class
    
    @classmethod
    def get_available_puzzles(cls) -> List[str]:
        """Get list of available puzzle types"""
        return list(cls._puzzles.keys())
    
    @classmethod
    def create_puzzle(cls, puzzle_type: str, difficulty: str = "medium") -> Puzzle:
        """Create a puzzle instance"""
        if puzzle_type not in cls._puzzles:
            raise ValueError(f"Unknown puzzle type: {puzzle_type}")
        return cls._puzzles[puzzle_type](difficulty=difficulty)
