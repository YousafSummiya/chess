class BoardMovement:
    @staticmethod
    def forward(position: str, color: str, squares: int = 1):
        """Move forward (WHITE: up rows, BLACK: down rows)."""
        column = position[0]
        row = int(position[1])
        
        # WHITE moves up (increase row), BLACK moves down (decrease row)
        if color == "WHITE":
            new_row = min(row + squares, 8)
        else:  # BLACK
            new_row = max(row - squares, 1)
            
        if new_row == row:  # Hit board edge
            return None
        return f"{column}{new_row}"

    @staticmethod
    def backward(position: str, color: str, squares: int = 1):
        """Move backward."""
        column = position[0]
        row = int(position[1])
        
        if color == "WHITE":
            new_row = max(row - squares, 1)
        else:
            new_row = min(row + squares, 8)
            
        if new_row == row:
            return None
        return f"{column}{new_row}"

    @staticmethod
    def left(position: str, squares: int = 1):
        """Move left."""
        column = position[0]
        row = int(position[1])
        col_idx = ord(column) - ord('a')
        
        new_col_idx = max(col_idx - squares, 0)
        new_column = chr(ord('a') + new_col_idx)
        
        if new_col_idx == col_idx:
            return None
        return f"{new_column}{row}"

    @staticmethod
    def right(position: str, squares: int = 1):
        """Move right."""
        column = position[0]
        row = int(position[1])
        col_idx = ord(column) - ord('a')
        
        new_col_idx = min(col_idx + squares, 7)
        new_column = chr(ord('a') + new_col_idx)
        
        if new_col_idx == col_idx:
            return None
        return f"{new_column}{row}"

    @staticmethod
    def forward_left(position: str, color: str, squares: int = 1):
        """Diagonal forward-left."""
        forward_pos = BoardMovement.forward(position, color, squares)
        left_pos = BoardMovement.left(position, squares)
        if forward_pos and left_pos:
            col = forward_pos[0]
            row_str = left_pos[1:]
            return f"{col}{row_str}"
        return None

    @staticmethod
    def forward_right(position: str, color: str, squares: int = 1):
        """Diagonal forward-right."""
        forward_pos = BoardMovement.forward(position, color, squares)
        right_pos = BoardMovement.right(position, squares)
        if forward_pos and right_pos:
            col = forward_pos[0]
            row_str = right_pos[1:]
            return f"{col}{row_str}"
        return None

    @staticmethod
    def backward_left(position: str, color: str, squares: int = 1):
        """Diagonal backward-left."""
        backward_pos = BoardMovement.backward(position, color, squares)
        left_pos = BoardMovement.left(position, squares)
        if backward_pos and left_pos:
            col = backward_pos[0]
            row_str = left_pos[1:]
            return f"{col}{row_str}"
        return None

    @staticmethod
    def backward_right(position: str, color: str, squares: int = 1):
        """Diagonal backward-right."""
        backward_pos = BoardMovement.backward(position, color, squares)
        right_pos = BoardMovement.right(position, squares)
        if backward_pos and right_pos:
            col = backward_pos[0]
            row_str = right_pos[1:]
            return f"{col}{row_str}"
        return None
