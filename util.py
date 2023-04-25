import chess
import chess.svg


def play_game(board, white_player, black_player, display, last_move=None):
    display(board)
    while not board.is_game_over():
        player = white_player if board.turn == chess.WHITE else black_player
        move = player.play(board)
        board.push(move)
        display(board)
    return board


def text_display(board, last_move):
    print("\n-------")
    print(board)
    print("-------\n")


def svg_display(board):
    move = board.peek() if len(board.move_stack) else None
    chess.svg.board(board, lastmove=move, size=300)


def position_features(board):
    piece_map = board.piece_map()
    turn = board.turn
