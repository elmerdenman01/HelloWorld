"""
Tests for puzzle generation
"""
import unittest
from puzzlebook.puzzle_base import PuzzleRegistry
from puzzlebook.puzzles.sudoku import SudokuPuzzle
from puzzlebook.puzzles.wordsearch import WordSearchPuzzle
from puzzlebook.puzzles.crossword import CrosswordPuzzle
from puzzlebook.puzzles.maze import MazePuzzle


class TestPuzzleRegistry(unittest.TestCase):
    """Test the puzzle registry"""
    
    def test_get_available_puzzles(self):
        """Test getting list of available puzzles"""
        puzzles = PuzzleRegistry.get_available_puzzles()
        self.assertIsInstance(puzzles, list)
        self.assertGreater(len(puzzles), 0)
        self.assertIn("Sudoku", puzzles)
        self.assertIn("Word Search", puzzles)
        self.assertIn("Crossword", puzzles)
        self.assertIn("Maze", puzzles)
    
    def test_create_puzzle(self):
        """Test creating puzzle instances"""
        sudoku = PuzzleRegistry.create_puzzle("Sudoku", "easy")
        self.assertIsInstance(sudoku, SudokuPuzzle)
        self.assertEqual(sudoku.difficulty, "easy")
        
        wordsearch = PuzzleRegistry.create_puzzle("Word Search", "medium")
        self.assertIsInstance(wordsearch, WordSearchPuzzle)
        self.assertEqual(wordsearch.difficulty, "medium")
    
    def test_create_invalid_puzzle(self):
        """Test creating invalid puzzle type"""
        with self.assertRaises(ValueError):
            PuzzleRegistry.create_puzzle("NonExistentPuzzle")


class TestSudokuPuzzle(unittest.TestCase):
    """Test Sudoku puzzle generation"""
    
    def test_generate(self):
        """Test Sudoku generation"""
        puzzle = SudokuPuzzle(difficulty="easy")
        data = puzzle.generate()
        
        self.assertIn('grid', data)
        self.assertIn('difficulty', data)
        self.assertEqual(len(data['grid']), 9)
        self.assertEqual(len(data['grid'][0]), 9)
    
    def test_to_html(self):
        """Test Sudoku HTML generation"""
        puzzle = SudokuPuzzle(difficulty="medium")
        html = puzzle.to_html()
        
        self.assertIn('<table class="sudoku-grid">', html)
        self.assertIn('Sudoku', html)
        self.assertIn('Medium', html)


class TestWordSearchPuzzle(unittest.TestCase):
    """Test Word Search puzzle generation"""
    
    def test_generate(self):
        """Test Word Search generation"""
        puzzle = WordSearchPuzzle(difficulty="easy")
        data = puzzle.generate()
        
        self.assertIn('grid', data)
        self.assertIn('words', data)
        self.assertIn('difficulty', data)
        self.assertGreater(len(data['words']), 0)
    
    def test_to_html(self):
        """Test Word Search HTML generation"""
        puzzle = WordSearchPuzzle(difficulty="hard")
        html = puzzle.to_html()
        
        self.assertIn('<table class="word-search-grid">', html)
        self.assertIn('Word Search', html)
        self.assertIn('Find these words:', html)


class TestCrosswordPuzzle(unittest.TestCase):
    """Test Crossword puzzle generation"""
    
    def test_generate(self):
        """Test Crossword generation"""
        puzzle = CrosswordPuzzle(difficulty="medium")
        data = puzzle.generate()
        
        self.assertIn('clues', data)
        self.assertIn('across', data['clues'])
        self.assertIn('down', data['clues'])
    
    def test_to_html(self):
        """Test Crossword HTML generation"""
        puzzle = CrosswordPuzzle(difficulty="easy")
        html = puzzle.to_html()
        
        self.assertIn('Crossword', html)
        self.assertIn('Across', html)
        self.assertIn('Down', html)


class TestMazePuzzle(unittest.TestCase):
    """Test Maze puzzle generation"""
    
    def test_generate(self):
        """Test Maze generation"""
        puzzle = MazePuzzle(difficulty="easy")
        data = puzzle.generate()
        
        self.assertIn('maze', data)
        self.assertIn('size', data)
        self.assertIn('start', data)
        self.assertIn('end', data)
    
    def test_to_html(self):
        """Test Maze HTML generation"""
        puzzle = MazePuzzle(difficulty="hard")
        html = puzzle.to_html()
        
        self.assertIn('<table class="maze-grid">', html)
        self.assertIn('Maze', html)


if __name__ == '__main__':
    unittest.main()
