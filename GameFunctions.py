from Color import Color
from Board import Board

class GameFunctions():
    '''
    This class defined the game functions that will be utilized in our connect four game. 
    '''

    def __init__(self):
        '''
        initiates the needed components of our connect four game. 
        '''
        self.player1 = Color.RED
        self.player2 = Color.YELLOW
        self.turn = -1
        self.board = Board()
        self.switch_turns()

    def switch_turns(self):
        '''
        Switches the players turn and returns who's turn it is in a message. 
        
        :return: calls the get_turn_message to return whos turn it is in a string. 
        '''
        self.turn = self.turn * -1  
        return self.get_turn_message()

    def get_turn_message(self):
        '''
        The message function that returns a string of whos turn it is to play on the board. 
        '''
        if self.turn == 1:
            print(f"It's {self.player1.name}'s turn!")
            return(f"It's {self.player1.name}'s turn!")
        else:
            print(f"It's {self.player2.name}'s turn!")
            return(f"It's {self.player2.name}'s turn!")
       
       
        
    def playTile(self, column):
        '''
        This function keeps track of whether or not the game ended by utilizing the checkWin function. 
        When a player drops a tile, this function checks if it has resulted in a win and returns true, and if not, switches the 
        players turn and returns false instead. 
        
        :param column: the column the player has selected to drop their piece. 
        :return: returns true if a player has won the game by calling the checkWin function. 
        '''
        if(self.board.dropTile(column, Color(self.turn))):
            win = [False]
            if(self.checkWin()):
                win = [True, self.getCurrentPlayer()]
            self.switch_turns()
            return win


    def getCurrentPlayer(self):
        '''
        This function checks which player is up for a turn on our board. 
        :returns: the player who is up for a turn. 
        '''
        if(self.turn < 0):
            return self.player2
        else:
            return self.player1      

    def checkWin(self):
        '''
        Checks all of our possible winning combinations of connecting four matching pieces on the board. 
        :return: returns true if one of our winning combinations are met. 
        '''
        return(self.board.checkRows() or self.board.checkColumns() or self.board.checkRightDiagonals() or self.board.checkLeftDiagonals())

    