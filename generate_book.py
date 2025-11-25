#!/usr/bin/env python3
"""
Puzzle Book Generator - CLI Interface
Create custom puzzle books for Amazon Kindle publishing
"""
import sys
from puzzlebook.book_builder import PuzzleBookBuilder


def display_menu():
    """Display the main menu"""
    print("\n" + "="*50)
    print("  PUZZLE BOOK GENERATOR FOR AMAZON KINDLE")
    print("="*50)
    print("\nAvailable Puzzle Types:")
    
    available_puzzles = PuzzleBookBuilder.get_available_puzzle_types()
    for i, puzzle_type in enumerate(available_puzzles, 1):
        print(f"  {i}. {puzzle_type}")
    
    print("\nOptions:")
    print("  - Enter puzzle numbers (comma-separated) to include")
    print("  - Or 'all' to include all puzzle types")
    print("  - Or 'quit' to exit")


def get_user_input():
    """Get user input for puzzle selection"""
    display_menu()
    
    available_puzzles = PuzzleBookBuilder.get_available_puzzle_types()
    
    while True:
        selection = input("\nYour selection: ").strip().lower()
        
        if selection == 'quit':
            print("Exiting...")
            sys.exit(0)
        
        if selection == 'all':
            return available_puzzles
        
        # Parse comma-separated numbers
        try:
            numbers = [int(x.strip()) for x in selection.split(',')]
            selected_puzzles = []
            for num in numbers:
                if 1 <= num <= len(available_puzzles):
                    selected_puzzles.append(available_puzzles[num - 1])
                else:
                    print(f"Invalid number: {num}")
                    break
            else:
                if selected_puzzles:
                    return selected_puzzles
        except ValueError:
            pass
        
        print("Invalid selection. Please try again.")


def get_book_details():
    """Get book title and other details"""
    print("\n" + "-"*50)
    title = input("Enter book title (or press Enter for default): ").strip()
    if not title:
        title = "My Puzzle Book"
    
    difficulty = input("Select difficulty (easy/medium/hard, or press Enter for medium): ").strip().lower()
    if difficulty not in ['easy', 'medium', 'hard']:
        difficulty = 'medium'
    
    try:
        count = int(input("How many puzzles of each type? (default: 5): ").strip() or "5")
    except ValueError:
        count = 5
    
    return title, difficulty, count


def main():
    """Main CLI application"""
    print("\nWelcome to Puzzle Book Generator!")
    
    # Get puzzle selection
    selected_puzzles = get_user_input()
    
    print(f"\nYou selected: {', '.join(selected_puzzles)}")
    
    # Get book details
    title, difficulty, count = get_book_details()
    
    # Build the book
    print("\n" + "="*50)
    print("Building your puzzle book...")
    print("="*50)
    
    builder = PuzzleBookBuilder(title=title)
    
    for puzzle_type in selected_puzzles:
        print(f"  Adding {count} {puzzle_type} puzzles ({difficulty})...")
        builder.add_puzzles(puzzle_type, count=count, difficulty=difficulty)
    
    # Save to file
    filename = builder.save_to_file()
    
    print("\n" + "="*50)
    print("SUCCESS!")
    print("="*50)
    print(f"\nYour puzzle book has been created!")
    print(f"File: {filename}")
    print(f"\nTotal puzzles: {len(builder.puzzles)}")
    print(f"\nYou can now:")
    print("  1. Open the HTML file in a web browser")
    print("  2. Print to PDF for Kindle upload")
    print("  3. Use a converter tool to create MOBI format")
    print("\nReady for Amazon Kindle publishing!")
    print("\n")


if __name__ == "__main__":
    main()
