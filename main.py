from HumanPlayer import HumanPlayer
from Board import Board
import gc

global board
global human
global nextState



def main():
    global board,human, nextState
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
                ComputerChoice()
                printState(nextState)
                CleanBoard()
        else:
            while True:
                board.buildBoardTree(nextState)
                ComputerChoice()
                CleanBoard()
                printState(nextState)
                HumanChoice()
                printState(nextState)
                CleanBoard()




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
    print('*            Welcome To Connect Four!!          *')
    print('*************************************************')
    print('*                  Game Modes                   *')
    print('*************************************************')
    print('1. Player vs Player')
    print('2. Player vs Computer')
    print('*************************************************')

if __name__ == "__main__":
    main()