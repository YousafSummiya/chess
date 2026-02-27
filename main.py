from board import Board

if __name__ == "__main__":
    print("=== Testing REAL Movements ===\n")
    
    board = Board()
    print("Initial board:")
    board.print_board()
    print("\n" + "="*60 + "\n")
    
    # Test WHITE pawn e7 -> e6
    white_pawn_e7 = board.get_piece('e7')
    print("1. WHITE Pawn e7 moves forward:")
    white_pawn_e7.move()
    board.print_board()
    
    print("\n" + "="*60 + "\n")
    
    # Test BLACK pawn e2 -> e3  
    black_pawn_e2 = board.get_piece('e2')
    print("2. BLACK Pawn e2 moves forward:")
    black_pawn_e2.move()
    board.print_board()
