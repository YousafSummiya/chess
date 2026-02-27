from board import Board
from movements import BoardMovement
import os

def clear_board_txt():
    if os.path.exists('board.txt'):
        os.remove('board.txt')
        print("  Cleared board.txt")

board = Board()
current_player = "WHITE"
move_count = 0

print("  INTERACTIVE CHESS GAME")
print("Commands: e7 e6, board, clear, quit")
print(f"Turn: {current_player}\n")

while True:
    print(f"\n--- Move #{move_count + 1} ({current_player}) ---")
    board.print_board()
    
    cmd = input("\nYour move: ").strip().lower()
    
    if cmd == 'quit':
        print("\n👋 Thanks for playing!")
        break
    elif cmd == 'board':
        board.print_board()
        continue
    elif cmd == 'clear':
        clear_board_txt()
        continue
    elif len(cmd.split()) == 2:
        try:
            from_sq, to_sq = cmd.split()
            piece = board.get_piece(from_sq)
            
            if not piece:
                print(f"Empty at {from_sq}")
            elif piece.color != current_player:
                print(f" {piece.color}'s piece! Your turn: {current_player}")
            else:
                print(f"\n{piece} from {from_sq} → {to_sq}")
                if piece.move(to_sq):
                    move_count += 1
                    current_player = "BLACK" if current_player == "WHITE" else "WHITE"
                    print(f" {current_player}'s turn!")
        except:
            print(" Format: e7 e6")
    else:
        print(" Try: e7 e6, board, quit")

print(f"\n Game over! {move_count} moves played.")
print(f" {move_count} states saved in board.txt")
