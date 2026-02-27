from typing import Tuple

class BoardMovement:
    @staticmethod
    def forward(position: str, color: str, squares: int = 1):
        col, row = position[0], int(position[1])
        direction = -1 if color == 'WHITE' else 1  # White moves up (decreasing row)
        new_row = max(1, min(8, row + direction * squares))
        return f"{col}{new_row}"

    @staticmethod
    def backward(position: str, color: str, squares: int = 1):
        col, row = position[0], int(position[1])
        direction = 1 if color == 'WHITE' else -1
        new_row = max(1, min(8, row + direction * squares))
        return f"{col}{new_row}"

    @staticmethod
    def left(position: str, squares: int = 1):
        col, row = position[0], int(position[1])
        new_col = max('a', chr(max(ord('a'), ord(col) - squares)))
        return f"{new_col}{row}"

    @staticmethod
    def right(position: str, squares: int = 1):
        col, row = position[0], int(position[1])
        new_col = min('h', chr(min(ord('h'), ord(col) + squares)))
        return f"{new_col}{row}"


    @staticmethod
    def forward_left(position: str, color: str, squares: int = 1) -> str:
        """Diagonal forward-left"""
        col, row = position[0], int(position[1])
        direction = -1 if color == 'WHITE' else 1
        new_row = max(1, min(8, row + direction * squares))
        new_col_ord = max(ord('a'), ord(col) - squares)
        new_col = chr(new_col_ord)
        return f"{new_col}{new_row}"
