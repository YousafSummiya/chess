from board import Board, BoardMovements

# Create and setup board
board = Board()
board.setup_board()

print("=== FULL CHESS BOARD ===")
board.print_board()

print("\n=== HELPER FUNCTIONS ===")
print(f"White King e1: {board.get_piece('e1')}")
print(f"e4 empty: {board.is_square_empty('e4')}")
print(f"Black Rook a8: {board.find_piece('R', 1, 'BLACK')}")

print("\n=== MOVEMENT TEST ===")
print(BoardMovements.forward('e2', 'WHITE'))  # e3
print(BoardMovements.forward('e7', 'BLACK'))  # e6
print(BoardMovements.left('e4', 2))          # c4
