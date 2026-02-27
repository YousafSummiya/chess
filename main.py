from pieces import Pawn, Rook, Bishop, Queen, King, Knight

if __name__ == "__main__":
    print("=== Testing ALL Chess Pieces ===\n")
    
    pieces = [
        Pawn("BLACK", 1),
        Rook("WHITE", 1),
        Bishop("BLACK", 1),
        Queen("WHITE", 1),
        King("BLACK", 1),
        Knight("WHITE", 1)
    ]
    
    for piece in pieces:
        print(f"Created: {piece}")
        piece.move()
        print("-" * 30)
