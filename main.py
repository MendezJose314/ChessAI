import chess
import util
import DummyEngine

board = chess.Board()
move = None
util.play_game(board, DummyEngine.DummyEngine(), DummyEngine.DummyEngine(), util.svg_display(board), move)
