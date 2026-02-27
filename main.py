from pieces import Pawn

# Test inheritance - exactly as assignment specifies
pawn = Pawn("BLACK", 1)
print(pawn)  # Should output: BLACK Pawn 1
pawn.move("forward")  # Should output: Pawn moves forward 1 position
print(f"Pawn position: {pawn.position}")  # None
print(f"Pawn alive: {pawn.is_alive}")  # True
