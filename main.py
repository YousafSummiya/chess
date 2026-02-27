from pieces import Pawn, Rook, Bishop, Knight, King, Queen

print("=== Testing Inheritance ===\n")

# Test each piece
pieces = [
    Pawn("BLACK", 1),
    Rook("WHITE", 1),
    Bishop("BLACK", 1),
    Knight("WHITE", 1),
    King("BLACK", 1),
    Queen("WHITE", 1)
]

for piece in pieces:
    print(piece)
    piece.move("test")
    print()
