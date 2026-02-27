from board import Board
from movements import BoardMovement
from pieces import Pawn

if __name__ == "__main__":
    print("🎯 FIXED CHESS GAME - Choose mode:")
    print("1. Interactive game")
    print("2. Demo moves (GENERATES new board.txt)")
    print("3. Load saved states")
    
    choice = input("Enter 1-3: ").strip()
    
    if choice == "1":
        print("\n🛠️ Interactive game needs game.py - run demo first!")
        choice = "2"
    
    if choice == "2":
        print("\n=== DEMO GAME - Creates NEW board.txt ===")
        import os
        if os.path.exists('board.txt'):
            os.remove('board.txt')
            print("🗑️ Cleared old board.txt")
        
        board = Board()
        print("Initial board:")
        board.print_board()
        
        # ACTUAL MOVES THAT WORK
        white_pawn = board.get_piece('e7')
        print("\n1. White pawn e7 → e6:")
        white_pawn.move('e6')
        
        black_pawn = board.get_piece('e2')
        print("\n2. Black pawn e2 → e3:")
        black_pawn.move('e3')
        
        print("\n✅ Check board.txt was created:")
        print("Should now show ACTUAL moved positions!")
        
    elif choice == "3":
        print("\n=== LOAD GAME STATES ===")
        for state_num, state_dict in Board.load_board_states_generator():
            print(f"\n--- STATE #{state_num} ---")
            Board.print_state_from_generator(state_dict)
            if state_num >= 2:
                break
    else:
        board = Board()
        board.print_board()
