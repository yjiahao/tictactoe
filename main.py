# user will input which position to input the x or O (rmb to add 1 because of indexing)
# everytime after a turn, you need to check whether someone has won the game (check scenarios)
# can i play vs a bot? maybe like a random module to choose which positions?
import random

class TicTacToe:

    def __init__(self):
        self.board = []
        self.player_num = 0
        self.turns = 0
        self.resume = True

    def create_board(self):
        num = 0
        for i in range(3):
            row = []
            for j in range(3):
                row.append('-')
            self.board.append(row)

    def show_board(self):
        column_num = 1
        for row in self.board:
            for position in row:
                if column_num % 3 == 0:
                    print(position)
                else:
                    print(position, end=' ')
                column_num += 1

    def ask_for_moves(self):
        while self.resume:
            if self.turns % 2 == 0:
                row = int(input('Player 1: Which row would you like to place your move?')) - 1
                column = int(input('Player 1: Which column would you like to place your move?')) - 1
            elif self.turns % 2 != 0:
                row = int(input('Player 2: Which row would you like to place your move?')) - 1
                column = int(input('Player 2: Which column would you like to place your move?')) - 1
            # Checking if the rows or columns are out of the 3 by 3 range
            if row > 2 or column > 2 and row < 0 or column < 0:
                print('Your inputs are out of range! Please try again!')
                return self.ask_for_moves()
            # Checking if the spot is already taken by 'X' or 'O'
            # if self.board[row][column] != '-':
            #     print('\nThat spot is already taken! Please try again!')
            #     return self.ask_for_moves()
            self.update_board(row=row, column=column)
            self.game_is_over()
            self.turns += 1

    def update_board(self, row, column):
        if self.board[row][column] != '-':
            print('\nThat spot is already taken! Please try again!')
            return self.ask_for_moves()
        for horiztonal_pos in self.board:
            for vertical_pos in horiztonal_pos:
                if self.turns % 2 == 0:
                    self.board[row][column] = 'X'
                elif self.turns % 2 != 0:
                    self.board[row][column] = 'O'
        self.show_board()

    def game_is_over(self):
        # Check if rows got anyone win
        for row in self.board:
            if row == ['O', 'O', 'O']:
                self.resume = False
                print('Player 2 wins!')
            elif row == ['X', 'X', 'X']:
                self.resume = False
                print('Player 1 wins!')
        # Check if column got anyone win (Hardcoded)
        # Column 1
        if self.board[0][0] == 'X' and self.board[1][0] == 'X' and self.board[2][0] == 'X':
            self.resume = False
            print('Player 1 wins!')
        elif self.board[0][0] == 'O' and self.board[1][0] == 'O' and self.board[2][0] == 'O':
            self.resume = False
            print('Player 2 wins!')
        # Column 2
        elif self.board[0][1] == 'X' and self.board[1][1] == 'X' and self.board[2][1] == 'X':
            self.resume = False
            print('Player 1 wins!')
        elif self.board[0][1] == 'O' and self.board[1][1] == 'O' and self.board[2][1] == 'O':
            self.resume = False
            print('Player 2 wins!')
        # Column 3
        elif self.board[0][2] == 'X' and self.board[1][2] == 'X' and self.board[2][2] == 'X':
            self.resume = False
            print('Player 1 wins!')
        elif self.board[0][2] == 'O' and self.board[1][2] == 'O' and self.board[2][2] == 'O':
            self.resume = False
            print('Player 2 wins!')
        # Diagonal part
        elif self.board[0][0] == 'X' and self.board[1][1] == 'X' and self.board[2][2] == 'X':
            self.resume = False
            print('Player 1 wins')
        elif self.board[0][0] == 'O' and self.board[1][1] == 'O' and self.board[2][2] == 'O':
            self.resume = False
            print('Player 2 wins')
        # Bottom up diagonal
        elif self.board[0][2] == 'X' and self.board[1][1] == 'X' and self.board[2][0] == 'X':
            self.resume = False
            print('Player 1 wins')
        elif self.board[0][2] == 'O' and self.board[1][1] == 'O' and self.board[2][0] == 'O':
            self.resume = False
            print('Player 2 wins')
        else:
            num_rows_filled = 0
            for row in self.board:
                if '-' not in row:
                    num_rows_filled += 1
            if num_rows_filled == 3:
                self.resume = False
                print('It\'s a draw, no one won!')

    def start_game(self):
        self.create_board()
        self.show_board()
        self.ask_for_moves()


game = TicTacToe()
game.start_game()

# Able to choose between player 1 or 2 now, but what if you play against bot?
# How to know who will start the game? Player 1 or 2?
# Maybe do a random.randint then choose between 1 or 2

# Making the game disallow players to put ontop of a preoccupied position:
# do like an if statement before updating of the list and check if the spot == '-'
# else then ask him repeat his move again (while loop)
