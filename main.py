from pieces import Pawn

# Test inheritance
pawn = Pawn("BLACK", 1)
print(pawn)  # Output: BLACK Pawn 1
pawn.move("forward")  # Output: Pawn moves forward 1 position
print(pawn.is_alive)  # Output: True
pawn.die()
print(pawn.is_alive)  # Output: False
