from board import Board
from pieces import *
from board_movements import BoardMovements

def main():
    print("🐎 CHESS GAME - OOP Python Demo 🐎")
    print("=" * 50)
    
    # Create board
    board = Board()
    
    print("1. INITIAL BOARD STATE:")
    board.print_board()
    
    print("\n" + "="*50)
    print("2. TEST HELPER METHODS:")
    
    # Test helper methods
    print(f"Piece on a1: {board.get_piece('a1')}")
    print(f"Is e4 empty? {board.is_square_empty('e4')}")
    print(f"Black Rook 1 found: {board.find_piece('R', 1, 'BLACK')}")
    
    print("\n" + "="*50)
    print("3. TEST MOVEMENTS (without board logic):")
    
    # Test individual pieces
    black_pawn = board.get_piece('a2')
    if black_pawn:
        black_pawn.move(black_pawn.calculate_move())
    
    white_rook = board.get_piece('a8')
    if white_rook:
        white_rook.move(white_rook.calculate_move('left', 2))
    
    print("\n" + "="*50)
    print("4. SAVE INITIAL STATE:")
    board.save_state()
    
    print("\n All features working!")
    print(" OOP Inheritance, Abstract Methods")
    print(" Dict/List Comprehensions")
    print(" Board setup & printing")
    print(" Helper methods implemented")

if __name__ == "__main__":
    main()
