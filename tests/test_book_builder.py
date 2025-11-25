"""
Tests for puzzle book builder
"""
import unittest
import os
from puzzlebook.book_builder import PuzzleBookBuilder


class TestPuzzleBookBuilder(unittest.TestCase):
    """Test the puzzle book builder"""
    
    def test_builder_initialization(self):
        """Test builder initialization"""
        builder = PuzzleBookBuilder(title="Test Book")
        self.assertEqual(builder.title, "Test Book")
        self.assertEqual(len(builder.puzzles), 0)
    
    def test_add_puzzles(self):
        """Test adding puzzles to the book"""
        builder = PuzzleBookBuilder()
        builder.add_puzzles("Sudoku", count=3, difficulty="easy")
        
        self.assertEqual(len(builder.puzzles), 3)
        self.assertEqual(builder.puzzles[0].puzzle_type, "Sudoku")
    
    def test_add_multiple_puzzle_types(self):
        """Test adding multiple puzzle types"""
        builder = PuzzleBookBuilder()
        builder.add_puzzles("Sudoku", count=2, difficulty="easy")
        builder.add_puzzles("Word Search", count=2, difficulty="medium")
        
        self.assertEqual(len(builder.puzzles), 4)
    
    def test_build_html(self):
        """Test HTML generation"""
        builder = PuzzleBookBuilder(title="Test Book")
        builder.add_puzzles("Sudoku", count=1, difficulty="easy")
        
        html = builder.build_html()
        
        self.assertIn('<!DOCTYPE html>', html)
        self.assertIn('Test Book', html)
        self.assertIn('Sudoku', html)
    
    def test_save_to_file(self):
        """Test saving to file"""
        builder = PuzzleBookBuilder(title="Test Book")
        builder.add_puzzles("Sudoku", count=1, difficulty="easy")
        
        filename = "test_output.html"
        try:
            result = builder.save_to_file(filename)
            self.assertEqual(result, filename)
            self.assertTrue(os.path.exists(filename))
            
            # Check file content
            with open(filename, 'r', encoding='utf-8') as f:
                content = f.read()
                self.assertIn('Test Book', content)
        finally:
            if os.path.exists(filename):
                os.remove(filename)
    
    def test_get_available_puzzle_types(self):
        """Test getting available puzzle types"""
        puzzles = PuzzleBookBuilder.get_available_puzzle_types()
        self.assertIsInstance(puzzles, list)
        self.assertGreater(len(puzzles), 0)


if __name__ == '__main__':
    unittest.main()
