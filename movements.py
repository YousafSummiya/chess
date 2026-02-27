class BoardMovements:
    """Static methods for all chess movements - NO IMPORTS!"""

    @staticmethod
    def forward(position, color, squares=1):
        col, row = position[0], int(position[1])
        delta = squares if color == 'WHITE' else -squares
        new_row = max(1, min(8, row + delta))
        return f"{col}{new_row}"

    @staticmethod
    def backward(position, color, squares=1):
        col, row = position[0], int(position[1])
        delta = -squares if color == 'WHITE' else squares
        new_row = max(1, min(8, row + delta))
        return f"{col}{new_row}"

    @staticmethod
    def left(position, squares=1):
        col, row = position[0], int(position[1])
        new_col = max(ord('a'), ord(col) - squares)
        return f"{chr(new_col)}{row}"

    @staticmethod
    def right(position, squares=1):
        col, row = position[0], int(position[1])
        new_col = min(ord('h'), ord(col) + squares)
        return f"{chr(new_col)}{row}"

    @staticmethod
    def forward_left(position, color, squares=1):
        col, row = position[0], int(position[1])
        delta = squares if color == 'WHITE' else -squares
        new_row = max(1, min(8, row + delta))
        new_col = max(ord('a'), ord(col) - squares)
        return f"{chr(new_col)}{new_row}"

    @staticmethod
    def forward_right(position, color, squares=1):
        col, row = position[0], int(position[1])
        delta = squares if color == 'WHITE' else -squares
        new_row = max(1, min(8, row + delta))
        new_col = min(ord('h'), ord(col) + squares)
        return f"{chr(new_col)}{new_row}"

    @staticmethod
    def backward_left(position, color, squares=1):
        col, row = position[0], int(position[1])
        delta = -squares if color == 'WHITE' else squares
        new_row = max(1, min(8, row + delta))
        new_col = max(ord('a'), ord(col) - squares)
        return f"{chr(new_col)}{new_row}"

    @staticmethod
    def backward_right(position, color, squares=1):
        col, row = position[0], int(position[1])
        delta = -squares if color == 'WHITE' else squares
        new_row = max(1, min(8, row + delta))
        new_col = min(ord('h'), ord(col) + squares)
        return f"{chr(new_col)}{new_row}"
