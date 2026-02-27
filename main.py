from board import Board

if __name__ == "__main__":
    print("=== Testing DECORATORS + AUTO BOARD PRINTING ===\n")
    
    board = Board()
    
    print("1. Move WHITE Pawn from e7:")
    white_pawn_e7 = board.get_piece('e7')
    white_pawn_e7.move()  # Auto-prints board before/after!
    
    print("\n2. Move BLACK Pawn from e2:")
    black_pawn_e2 = board.get_piece('e2')
    black_pawn_e2.move()  # Auto-saves to board.txt!
    
    print("\n3. Check board.txt was created:")
    try:
        with open('board.txt', 'r') as f:
            lines = f.readlines()
            print(f"board.txt created with {len(lines)} states saved!")
    except FileNotFoundError:
        print(" board.txt not found")
