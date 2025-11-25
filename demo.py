#!/usr/bin/env python3
"""
Demo script - Automatically generate a sample puzzle book
"""
from puzzlebook.book_builder import PuzzleBookBuilder


def main():
    """Generate a demo puzzle book"""
    print("Generating demo puzzle book...")
    print("="*50)
    
    # Create a builder
    builder = PuzzleBookBuilder(title="Demo Puzzle Book - Mixed Collection")
    builder.author = "Puzzle Book Generator Demo"
    
    # Add various puzzles
    print("Adding Sudoku puzzles (easy)...")
    builder.add_puzzles("Sudoku", count=3, difficulty="easy")
    
    print("Adding Word Search puzzles (medium)...")
    builder.add_puzzles("Word Search", count=3, difficulty="medium")
    
    print("Adding Crossword puzzles (medium)...")
    builder.add_puzzles("Crossword", count=2, difficulty="medium")
    
    print("Adding Maze puzzles (easy)...")
    builder.add_puzzles("Maze", count=2, difficulty="easy")
    
    # Save the book
    filename = builder.save_to_file("demo_puzzlebook.html")
    
    print("="*50)
    print(f"SUCCESS! Demo book created: {filename}")
    print(f"Total puzzles: {len(builder.puzzles)}")
    print("\nOpen the file in a web browser to view the puzzle book!")
    print("="*50)


if __name__ == "__main__":
    main()
