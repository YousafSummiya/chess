from board import Board
import os

if __name__ == "__main__":
    print("=== Testing GENERATORS + BOARD STATE LOADING ===\n")
    
    # Clear old board.txt if exists
    if os.path.exists('board.txt'):
        os.remove('board.txt')
        print("🗑️  Cleared old board.txt\n")
    
    board = Board()
    
    print("1. Make some moves to generate board states:")
    white_pawn = board.get_piece('e7')
    white_pawn.move()
    
    black_pawn = board.get_piece('e2')
    black_pawn.move()
    
    print("\n2. GENERATOR TEST - Loading board states one by one:")
    print(" Reading from board.txt using generator...\n")
    
    # Test generator - load states one at a time
    for state_num, state_dict in Board.load_board_states_generator():
        print(f"\n--- STATE #{state_num} ---")
        Board.print_state_from_generator(state_dict)
        print()
        if state_num >= 2:  # Show first 2 states only
            print("... (more states available)")
            break
    
    print("\n3. Generator memory efficiency demo:")
    print("This loads ONE line at a time - perfect for huge game logs!")
    
    total_states = sum(1 for _ in Board.load_board_states_generator())
    print(f" Total states saved: {total_states}")
