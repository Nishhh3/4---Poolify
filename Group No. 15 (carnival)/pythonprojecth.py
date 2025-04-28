import tkinter as tk
import chess  # Correct the import here

# Unicode pieces
PIECE_UNICODE = {
    'P': '♙', 'N': '♘', 'B': '♗', 'R': '♖', 'Q': '♕', 'K': '♔',
    'p': '♟', 'n': '♞', 'b': '♝', 'r': '♜', 'q': '♛', 'k': '♚'
}

class ChessApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Mouse-Controlled Chess")
        self.board = chess.Board()
        self.buttons = {}
        self.selected_square = None

        self.draw_board()

    def draw_board(self):
        for row in range(8):
            for col in range(8):
                square_index = chess.square(col, 7 - row)
                square_name = chess.square_name(square_index)
                piece = self.board.piece_at(square_index)
                symbol = PIECE_UNICODE.get(piece.symbol(), '') if piece else ''

                bg_color = "#EEEED2" if (row + col) % 2 == 0 else "#769656"

                btn = tk.Button(self.root,
                                text=symbol,
                                font=('Arial', 32),
                                width=2, height=1,
                                bg=bg_color,
                                command=lambda sq=square_name: self.on_click(sq))
                btn.grid(row=row, column=col)
                self.buttons[square_name] = btn

    def refresh_board(self):
        for square in chess.SQUARES:
            name = chess.square_name(square)
            piece = self.board.piece_at(square)
            symbol = PIECE_UNICODE.get(piece.symbol(), '') if piece else ''
            self.buttons[name]['text'] = symbol

            r, c = 7 - chess.square_rank(square), chess.square_file(square)
            color = "#EEEED2" if (r + c) % 2 == 0 else "#769656"
            self.buttons[name]['bg'] = color

    def on_click(self, square):
        if self.selected_square is None:
            piece = self.board.piece_at(chess.parse_square(square))
            if piece and piece.color == self.board.turn:
                self.selected_square = square
                self.buttons[square]['bg'] = "#F7EC65"  # highlight
        else:
            move_uci = self.selected_square + square
            move = chess.Move.from_uci(move_uci)
            if move in self.board.legal_moves:
                self.board.push(move)
            self.selected_square = None
            self.refresh_board()

if __name__ == '__main__':
    root = tk.Tk()
    app = ChessApp(root)
    root.mainloop()
