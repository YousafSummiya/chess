from board import Board

class ChessGame:
    def __init__(self):
        self.board = Board()
        self.current_turn = "WHITE"
        self.game_over = False
        
    def get_valid_moves(self, piece):
        """Get all valid moves for a piece (simplified)."""
        col_idx = ord(piece.position[0]) - ord('a')
        row = int(piece.position[1])
        
        moves = []
        
        if isinstance(piece, Pawn):
            target = BoardMovement.forward(piece.position, piece.color, 1)
            if target and (self.board.is_square_empty(target) or 
                          self.board.get_piece(target) and self.board.get_piece(target).color != piece.color):
                moves.append(target)
                
        elif isinstance(piece, Rook):
            # Forward/backward
            for i in range(1, 8):
                target = BoardMovement.forward(piece.position, piece.color, i)
                if not target: break
                moves.append(target)
                if self.board.get_piece(target): break
                
        elif isinstance(piece, Bishop):
            for i in range(1, 8):
                target = BoardMovement.forward_left(piece.position, piece.color, i)
                if not target: break
                moves.append(target)
                if self.board.get_piece(target): break
        
        elif isinstance(piece, Knight):
            knight_moves = [
                (1, 2), (1, -2), (-1, 2), (-1, -2),
                (2, 1), (2, -1), (-2, 1), (-2, -1)
            ]
            for dcol, drow in knight_moves:
                new_col_idx = col_idx + dcol
                new_row = row + drow if piece.color == "WHITE" else row - drow
                if 0 <= new_col_idx <= 7 and 1 <= new_row <= 8:
                    target = f"{chr(ord('a') + new_col_idx)}{new_row}"
                    moves.append(target)
        
        return [m for m in moves if m]

    def play(self):
        """Main game loop."""
        print("♟️  WELCOME TO INTERACTIVE CHESS! ♟️")
        print("Commands: 'move [piece] [target]' (e.g., 'move e7 e6')")
        print("Commands: 'board', 'quit', 'list [piece]'")
        print(f"Current turn: {self.current_turn}\n")
        
        while not self.game_over:
            self.board.print_board()
            print(f"\n{self.current_turn}'s turn> ", end="")
            
            try:
                cmd = input().strip().lower()
                
                if cmd == 'quit':
                    break
                elif cmd == 'board':
                    self.board.print_board()
                    continue
                elif cmd.startswith('list'):
                    piece_name = cmd.split()[1] if len(cmd.split()) > 1 else None
                    self.list_pieces(piece_name)
                    continue
                elif cmd.startswith('move'):
                    if not self.parse_move(cmd):
                        continue
                else:
                    print(" Invalid command! Use: move e2 e4, board, quit")
                    
            except KeyboardInterrupt:
                print("\n👋 Game ended!")
                break
        
        print(" Thanks for playing!")

    def parse_move(self, cmd: str) -> bool:
        """Parse move command like 'move e2 e4'."""
        parts = cmd.split()
        if len(parts) != 3 or parts[0] != 'move':
            print(" Format: move [from] [to] (e.g., 'move e2 e4')")
            return False
            
        from_square, to_square = parts[1], parts[2]
        
        if not (len(from_square) == 2 and len(to_square) == 2):
            print(" Invalid squares! Use a1-h8 format.")
            return False
            
        piece = self.board.get_piece(from_square)
        if not piece:
            print(f" No piece at {from_square}!")
            return False
            
        if piece.color != self.current_turn:
            print(f" Not your turn! {self.current_turn} plays now.")
            return False
            
        # Check if move is valid for this piece type
        valid_moves = self.get_valid_moves(piece)
        if to_square not in valid_moves:
            print(f" Invalid move for {piece}! Valid: {valid_moves[:3]}...")
            return False
        
        # Execute move
        success = piece.move(to_square)
        if success:
            self.current_turn = "BLACK" if self.current_turn == "WHITE" else "WHITE"
            print(f"\n {self.current_turn}'s turn!")
            return True
        return False

    def list_pieces(self, piece_filter=None):
        """List all pieces or filter by type."""
        print("\nYour pieces:")
        for square, piece in self.board.squares.items():
            if piece and piece.color == self.current_turn:
                moves = self.get_valid_moves(piece)
                print(f"{square}: {piece} → {moves[:2]}...")

