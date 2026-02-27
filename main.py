from pieces import Pawn, Rook, Bishop

if __name__ == "__main__":
    print("=== Testing Chess Pieces ===\n")
    
    # Create and test Pawn
    black_pawn = Pawn("BLACK", 1)
    print(f"Created: {black_pawn}")
    black_pawn.move()
    print()
    
    # Create and test Rook  
    white_rook = Rook("WHITE", 1)
    print(f"Created: {white_rook}")
    white_rook.move()
    print()
    
    # Create and test Bishop
    black_bishop = Bishop("BLACK", 1)
    print(f"Created: {black_bishop}")
    black_bishop.move()
