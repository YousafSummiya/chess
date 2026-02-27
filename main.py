from board import Board
from pieces import Pawn

if __name__ == "__main__":
    print("=== Testing Chess Board Setup ===\n")
    
    # Create board
    board = Board()
    
    # Print initial board state
    print("Initial board setup (White's perspective - row 8 to row 1):")
    board.print_board()
    print("\n" + "="*60 + "\n")
    
    # Test helper methods
    print("Testing helper methods:")
    print(f"Piece at e1: {board.get_piece('e1')}")
    print(f"Is a4 empty? {board.is_square_empty('a4')}")
    print(f"Find BLACK Rook 1: {board.find_piece('R', 1, 'BLACK')}")
