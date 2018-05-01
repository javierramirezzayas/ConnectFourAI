from HumanPlayer import HumanPlayer
from Board import Board

board = Board()
human = HumanPlayer()

print("Initial Connect Four Environment:\n")
answer = input("Do you want to start first?: ")

if answer.lower() == "yes":
    env = human.read(board.getInitialState())
    board.buildBoardTree(env)
else:
    board.buildBoardTree(board.getInitialState())


