import numpy as np
import sys

# Global Variables
ROW_COUNT = 6
COL_COUNT = 7
PLAYER1_TOKEN = 1
PLAYER2_TOKEN = 2


# Create an empty board.
def create_board():
    board = np.zeros((ROW_COUNT,COL_COUNT)) # Create a 6x7 matrix initialized wih zeros
    return board


# Drop piece through a column.
def drop_piece(board, row, col, piece):
    board[row][col] = piece


# Check if input is a valid column.
def check_valid_input(input):
    return (input >= 0) and (input <= COL_COUNT-1)


# Check whether the selected column is free.
def is_valid_column(board, col):
    return board[ROW_COUNT-1][col] == 0


# Check which row (closest to the bottom) is available.
def get_next_empty_row(board, col):
    for r in range(ROW_COUNT):
        if board[r][col] == 0:
            return r


# Print the board visible to the player.
def print_board(board):
    print(np.flip(board,0))
    print("  0  1  2  3  4  5  6")


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


# initializing variables
clear = lambda: print("\n" * 100)
reset = True

print("\nWelcome to Connect Four!!!\n")


# Game Definition
while reset:
    # Initializing variables to clear the game
    board = create_board()
    game_over = False
    turn_count = 0
    turn = 0

    while not game_over:
        print_board(board)
        print("Turn Count: ", turn_count)

        # Ask for Player 1 input
        if turn == 0:
            selected_col = int(input("Player 1, select a column (0-6): "))
            while not check_valid_input(selected_col):
                print(selected_col, " is an invalid input.")
                selected_col = int(input("Player 1, select a column (0-6): "))
            if is_valid_column(board, selected_col):
                row = get_next_empty_row(board, selected_col)
                drop_piece(board, row, selected_col, PLAYER1_TOKEN)
                clear()
                if winning_move(board, PLAYER1_TOKEN):
                    print_board(board)
                    print("Turn Count: ", turn_count)
                    print("PLAYER 1 WINS!!!")
                    game_over = True
                    response = input("Would you like to play again [y/n]: ")

        # Ask for Player 2 input
        else:
            selected_col = int(input("Player 2, select a column (0-6): "))
            while not check_valid_input(selected_col):
                selected_col = int(input("Player 2, select a column (0-6): "))
            if is_valid_column(board, selected_col):
                row = get_next_empty_row(board, selected_col)
                drop_piece(board, row, selected_col, PLAYER2_TOKEN)
                clear()
                if winning_move(board, PLAYER2_TOKEN):
                    print_board(board)
                    print("Turn Count: ", turn_count)
                    print("PLAYER 2 WINS!!!")
                    game_over = True
                    response = input("Would you like to play again [y/n]: ")

        # Select which player plays next turn
        turn += 1
        turn = turn % 2
        # Increase the turn count. To keep tack of how many turns has there been
        turn_count += 1



    if response == "n":
        print("Thank You for Playing!!!")
        reset = False

sys.exit()






