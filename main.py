from HumanPlayer import HumanPlayer
from Board import Board

board = Board()
human = HumanPlayer()
nextState = []
print('Welcome To Connect Four!!')
print('Game Modes:\n')
print('1. Player vs Player\n2. Player vs Computer\n')

answer = input('Select a Game Mode: ')

if answer == '2':
    answer = input("Do you want to start first?: ")
    if answer.lower() == "yes":
            env = human.read(board.getInitialState())
            board.buildBoardTree(env)
            board.displayGameBoard()

    else:
        board.buildBoardTree(board.getInitialState())
        board.displayGameBoard()

    while True:
        board.AIply()
        nextState = board.resetTree()
        del board
        board = Board()
        board.buildBoardTree(nextState)
        board.displayGameBoard()
        print('The Computer Has Made Its Move!')

        nextState = human.read(nextState)
        board.resetTree()
        del board
        board = Board()
        board.buildBoardTree(nextState)
        board.displayGameBoard()


