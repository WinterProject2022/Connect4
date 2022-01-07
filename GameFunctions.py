from Color import Color
from Board import Board

class GameFunctions():

    def __init__(self):
        self.player1 = Color.RED
        self.player2 = Color.YELLOW
        self.turn = -1
        self.board = Board()
        self.switch_turns()

    def switch_turns(self):
        self.turn = self.turn * -1  
        return self.get_turn_message()

    def get_turn_message(self):
        if self.turn == 1:
            print(f"It's {self.player1.name}'s turn!")
            return(f"It's {self.player1.name}'s turn!")
        else:
            print(f"It's {self.player2.name}'s turn!")
            return(f"It's {self.player2.name}'s turn!")
        
    def playTile(self, column):
        if(self.board.dropTile(column, Color(self.turn))):
            win = [False]
            if(self.checkWin()):
                win = [True, self.getCurrentPlayer()]
            self.switch_turns()
            return win

    def getCurrentPlayer(self):
        if(self.turn < 0):
            return self.player2
        else:
            return self.player1      

    def checkWin(self):
        return(self.board.checkRows() or self.board.checkColumns() or self.board.checkRightDiagonals() or self.board.checkLeftDiagonals())

    