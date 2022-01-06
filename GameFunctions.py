from Board import Board
class GameFunctions():
    turn = 0

    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
    
        

    def switch_turns(self):
        self.turn = self.turn % 2

        if self.turn == 0:
            print(f"It's {self.player1} turn!")
            self.turn += 1
        else:
            print(f"It's {self.player2} turn!")
            self.turn += 1
    
    def start_game(self):
        self.board = Board()

    def play(self, tile, column):
        self.board.dropTile(column, tile.color)
        

    