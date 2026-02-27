from board import Board

board = Board()
board.setup_board()

print("=== FULL CHESS BOARD ===")
board.print_board()

print("\n=== HELPER FUNCTIONS ===")
print(f"White King e1: {board.get_piece('e1')}")
print(f"e4 empty: {board.is_square_empty('e4')}")
print(f"Black Rook a8: {board.find_piece('R', 1, 'BLACK')}")

print("\n=== MOVEMENT TEST ===")
print("1. White Pawn e2 → e3:")
pawn = board.get_piece('e2')
pawn.move()

print("\n2. Black Queen d8 → backward 2 (clear path):")
queen = board.get_piece('d8')
queen.move("backward", 2)

print("\n3. Now Black Rook a8 → right 3:")
rook = board.get_piece('a8')
rook.move("right", 3)

print("\n=== REPLAY SAVED STATES ===")
for i, state in enumerate(Board.load_states()):
    if i < 3:
        print(f"State {i+1}: {list(state.items())[:4]}...")
