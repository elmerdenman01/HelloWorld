#!/usr/bin/env python3
"""
Simple test/validation script to verify core functionality
"""
from puzzlebook.book_builder import PuzzleBookBuilder


def test_core_functionality():
    """Test that all core features work correctly"""
    print("Testing Puzzle Book Generator...")
    print("="*50)
    
    # Test 1: Get available puzzles
    print("\nTest 1: Getting available puzzle types...")
    puzzles = PuzzleBookBuilder.get_available_puzzle_types()
    print(f"✓ Found {len(puzzles)} puzzle types: {', '.join(puzzles)}")
    assert len(puzzles) == 4, "Should have 4 puzzle types"
    
    # Test 2: Create a builder
    print("\nTest 2: Creating puzzle book builder...")
    builder = PuzzleBookBuilder(title="Test Book")
    print(f"✓ Builder created with title: {builder.title}")
    
    # Test 3: Add puzzles of each type
    print("\nTest 3: Adding puzzles of each type...")
    for puzzle_type in puzzles:
        builder.add_puzzles(puzzle_type, count=1, difficulty="medium")
        print(f"✓ Added {puzzle_type}")
    
    assert len(builder.puzzles) == 4, "Should have 4 puzzles total"
    print(f"✓ Total puzzles added: {len(builder.puzzles)}")
    
    # Test 4: Build HTML
    print("\nTest 4: Building HTML output...")
    html = builder.build_html()
    assert len(html) > 1000, "HTML should be substantial"
    assert "Test Book" in html, "Title should be in HTML"
    print(f"✓ HTML generated ({len(html)} characters)")
    
    # Test 5: Save to file
    print("\nTest 5: Saving to file...")
    filename = "validation_test.html"
    result = builder.save_to_file(filename)
    print(f"✓ File saved: {result}")
    
    # Clean up
    import os
    if os.path.exists(filename):
        os.remove(filename)
        print(f"✓ Test file cleaned up")
    
    print("\n" + "="*50)
    print("ALL TESTS PASSED! ✓")
    print("="*50)
    print("\nThe puzzle book generator is working correctly!")
    print("You can now use:")
    print("  - python generate_book.py (interactive)")
    print("  - python demo.py (quick demo)")


if __name__ == "__main__":
    test_core_functionality()
