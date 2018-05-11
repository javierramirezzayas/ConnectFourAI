from HumanPlayer import HumanPlayer
from Board import Board
import gc

global board
global human
global nextState
global ROW_COUNT
global COL_COUNT
global PLAYER1_TOKEN
global PLAYER2_TOKEN

ROW_COUNT = 6
COL_COUNT = 7
PLAYER1_TOKEN = 1
PLAYER2_TOKEN = 2


def main():
    global board, human, nextState
    board = Board()
    human = HumanPlayer()
    nextState = board.getInitialState()
    gc.enable()
    displayTitle()
    answer = input('Select a Game Mode: ')
    if answer == '2':
        print('\nPlayer vs Computer Mode')
        for row in nextState:
            print(row)
        answer = input("\nDo you want to start first?(yes/no): ")
        if answer.lower() == "yes":
            while True:
                HumanChoice()
                board.buildBoardTree(nextState)
                printState(nextState)
                if winning_move(nextState, PLAYER1_TOKEN):
                    print("Player 1 Wins!!!")
                    break
                ComputerChoice()
                printState(nextState)
                if winning_move(nextState, PLAYER2_TOKEN):
                    print("Player 2 Wins!!!")
                    break
                CleanBoard()
        else:
            while True:
                board.buildBoardTree(nextState)
                ComputerChoice()
                CleanBoard()
                printState(nextState)
                if winning_move(nextState, PLAYER1_TOKEN):
                    print("Player 1 Wins!!!")
                    break
                HumanChoice()
                printState(nextState)
                if winning_move(nextState, PLAYER2_TOKEN):
                    print("Player 2 Wins!!!")
                    break
                CleanBoard()


# Check if there is a win
def winning_move(board, piece):
    # Check horizontal locations for win
    for c in range(COL_COUNT-3):
        for r in range(ROW_COUNT):
            if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
                return True

    # Check vertical locations for win
    for c in range(COL_COUNT):
        for r in range(ROW_COUNT-3):
            if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
                return True

    # Check diagonal up for win
    for c in range(COL_COUNT-3):
        for r in range(ROW_COUNT-3):
            if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
                return True

    # Check diagonal down for win
    for c in range(COL_COUNT - 3):
        for r in range(3, ROW_COUNT):
            if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r+3][c+3] == piece:
                return True


def ComputerChoice():
    global board, nextState
    nextState = board.AIply()

def HumanChoice():
    global board, nextState, human
    nextState = human.read(nextState)

def CleanBoard():
    global board
    del board
    board = Board()

def printState(state):
    for row in state:
        print(row)
    print('\n')

def displayTitle():
    print('*************************************************')
    print('             Welcome To Connect Four!!           ')
    print('*************************************************')
    print('                   Game Modes                    ')
    print('*************************************************')
    print('1. Player vs Player')
    print('2. Player vs Computer')
    print('*************************************************')

if __name__ == "__main__":
    main()