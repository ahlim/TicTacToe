#Player class to identify individuals

class Player:
    def __init__(self, name):
        self.name = name
    
    def __repr__(self):
        return self.name

#Board class for board attributes
class Board:
    board = {1:1, 2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8, 9:9}

    def change_board(self, letter, square):
        self.board[square] = letter

    def check_board(self, square):
        if self.board[square] == "X" or self.board[square] == "O":
            return True
        return False

    def check_win(self):
        # first 3 rows
        if self.board[1] == self.board[2] and self.board[2] == self.board[3]:
            return True
        if self.board[4] == self.board[5] and self.board[5] == self.board[6]:
            return True
        if self.board[7] == self.board[8] and self.board[8] == self.board[9]:
            return True
        
        # first 3 cols
        if self.board[1] == self.board[4] and self.board[4] == self.board[7]:
            return True
        if self.board[2] == self.board[5] and self.board[5] == self.board[8]:
            return True
        if self.board[3] == self.board[6] and self.board[6] == self.board[9]:
            return True
        
        # diagonals
        if self.board[1] == self.board[5] and self.board[5] == self.board[9]:
            return True
        if self.board[3] == self.board[5] and self.board[5] == self.board[7]:
            return True

        return False        

    def print_board(self):
        print("| {} | {} | {} |".format(self.board[1], self.board[2], self.board[3]))
        print("|---|---|---|")
        print("| {} | {} | {} |".format(self.board[4], self.board[5], self.board[6]))
        print("|---|---|---|")
        print("| {} | {} | {} |\n".format(self.board[7], self.board[8], self.board[9]))

def play_game():
    x = input("Player 1, enter your name: ")
    player1 = Player(x)
    y = input("Player 2, enter your name: ")
    player2 = Player(y)
    print("welcome {} and {} to TicTacToe. May the best player win!!\n".format(player1, player2))
    board = Board()
    board.print_board()

    for turn in range(9):
        if turn % 2 == 0:
            while True:
                square = input("{} 'X': Choose a square number from 1 through 9 inclusive: ".format(player1))
                try:
                    int(square)
                except ValueError:
                    print("Error, pick a numeric value from 1 to 9 inclusive.\n")
                    continue
                if int(square) < 1 or int(square) > 9:
                    print("The value must be from 1 to 9 inclusive. Try again!\n")
                    continue
                if board.check_board(int(square)):
                    print("That square has been taken, try again!\n")
                    continue
                break
            board.change_board("X", int(square))
            if board.check_win():
                board.print_board()
                print("EYOO!!! {} you have Triumphed!!! Good Game!!!".format(player1))
                break
        else:
            while True:
                square = input("{} 'O': Choose a square number from 1 through 9 inclusive: ".format(player2))
                try:
                    int(square)
                except ValueError:
                    print("Pick a number from 1 to 9 inclusive.\n")
                    continue
                if int(square) < 1 or int(square) > 9:
                    print("The value must be from 1 to 9 inclusive. Try again!\n")
                    continue
                if board.check_board(int(square)):
                    print("That square has been taken, try again!\n")
                    continue
                break
            board.change_board("O", int(square))
            if board.check_win():
                board.print_board()
                print("EYOO!!! {} you have Triumphed!!! Good Game!!!".format(player2))
                break
        board.print_board()
    print("It's a draw!!! You both equally suck :)")
    


play_game()