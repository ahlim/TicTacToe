#Player class to identify individuals

class Player:
    def __init__(self, name):
        self.name = name
    
    def __repr__(self):
        return self.name

#Board class for board attributes
class Board:
    board = {1:1, 2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8, 9:9}

    def print_board(self):
        print("| {} | {} | {} |".format(self.board[1], self.board[2], self.board[3]))
        print("|---|---|---|")
        print("| {} | {} | {} |".format(self.board[4], self.board[5], self.board[6]))
        print("|---|---|---|")
        print("| {} | {} | {} |".format(self.board[7], self.board[8], self.board[9]))
        print("")

def play_game():
    x = input("Player 1, enter your name: ")
    player1 = Player(x)
    y = input("Player 2, enter your name: ")
    player2 = Player(y)
    print("welcome {} and {} to TicTacToe. May the best player win!!\n".format(player1, player2))
    board = Board()
    board.print_board()

play_game()