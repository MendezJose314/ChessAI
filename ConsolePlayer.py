import chess


class ConsolePlayer(object):
    def __init__(self):
        None

    def play(self, board):
        while True:
            try:
                # The name is from and to
                # So this will be from e2 to e4
                m = input("Enter your move (e.g., e2e4): ")
            except ValueError:
                print("Invalid move")
                m = None
            move = chess.Move.from_uci(m)
            if board.is_legal(move):
                break
            print("Illegal move!")
        return move
