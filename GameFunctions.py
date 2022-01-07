from Color import Color
from Board import Board

class GameFunctions():

    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.turn = -1
        self.board = Board()
        self.switch_turns()

    def switch_turns(self):
        self.turn = self.turn * -1  
        return self.get_turn_message()

    def get_turn_message(self):
        if self.turn == 1:
            print(f"It's {self.player1} turn!")
            return(f"It's {self.player1} turn!")
        else:
            print(f"It's {self.player2} turn!")
            return(f"It's {self.player2} turn!")
        
    def playTile(self, column):
        self.board.dropTile(column, Color(self.turn))
        self.switch_turns()      

    