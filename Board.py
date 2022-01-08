from Color import Color
from Tile import Tile

class Board(object):
    '''
    Creates an instance of our connect four board with a list of tiles. 
    
    '''
    def __init__(self):

        self.grid = [
            [],
            [],
            [],
            [],
            [],
            [],
            []
        ]

# This expands our Init Grid into a Board by visiting each column through our first 
# 'for loop' and the second 'for loop' is for expanding each column into having rows 
# by adding Tiles to that column in the range specified. 
        for column in range(len(self.grid)):
            for row in range(6):
                self.grid[column].append(Tile(Color.NONE, column, row))

   
   
   
    def dropTile(self, column, color):
        '''
        This function visits a column the user wishes to drop their connect
        four piece into and checks if there is a empty Tile in its row. If an empty
        Tile is found in the row, we will 'drop' the piece in that tile by switching the 
        color of the empty tile to the users color.
        
        :return: Whether or not a empty Tile was found, if found, changes the color of the tile and turns true. 
        '''
        for tile in self.grid[column]:
            if(tile.color == Color.NONE):
                tile.color = color
                return True
        return False



    def checkColumns(self):
        '''
        Checks if the Board has four tiles of the same color in a Column. If found returns true and that 
        player wins. 
        '''
       
        for column in self.grid:            #visits each column on the board through this for loop.
           
            counter = 0                     #sets initial count of matching pieces to 0.
            checkColor = Color.NONE         #sets the color to check matching pieces for a win. checkColor, changed in GameFunctions.py
            
          
            for tile in column:             # looks through each tile in the column through this for loop.
               
                 
                if(tile.color == Color.NONE):   #if initial tile is empty, this column is empty, thus we skip(break) and check the next column.
                    break
                
                if(checkColor == Color.NONE):   #resets our count to 1 if we find a empty tile in the column. 
                    counter = 1  #! -------------why is this not just set to 0? I can understand starting at 1 when we flip colors but when its empty it should be 0, no?
                
                elif(checkColor == tile.color): #add to matching count if players tile color found in column. 
                    counter += 1
                else:                           #resets our count to 1 if the column has the oppisite color found in the sequence of tiles for that column.
                    counter = 1
                checkColor = tile.color         #swithces colors to check if the other players color as a matching sequence in the column instead. 
            
                if(counter == 4):               #if a matching four tiles are found in the columns of our board, the player wins and we return true. 
                    return True       
        return False                            # returns false if a matching four tiles is NOT found in the columns of our board.


    def checkRows(self):
        '''
        Checks if the Board has four tiles of the same color in a Row. If found returns true and that 
        player wins. 
        '''
        
        for row in range(6):                  #first for loop checks the rows of each column. 
            counter = 0                       #count of matching pieces found. 
            checkColor = Color.NONE           #color of pieces we are finding matches for. 
          
            for column in self.grid:          #checks each column at the specified row from our last for loop. 
                tile = column[row]            #Sets tile to the same row of each column; we will use the first 'for loop' to always grab a certain row first, then visit that row in each column.  
                if(tile.color == Color.NONE): #skips/break this row when the first found tile is empty.
                    break

                if(checkColor == Color.NONE): #if the tile is empty then we reset the counter to 1. 
                    counter = 1
                elif(checkColor == tile.color): #add to matching count if players tile color found in row.
                    counter += 1
                else:                           #if another color tile is found in the row, then reset count to 1 and switch to other color to check for that color matching in a row instead. 
                    counter = 1
                checkColor = tile.color

                if(counter == 4):             #if a matching four tiles are found in the rows of our board, the player wins and we return true
                    return True
        return False                          # returns false if a matching four tiles is NOT found in the rows of our board.


    def checkRightDiagonals(self):
        '''
        Checks if the Board has four tiles of the same color in a Right Diagnol. If found returns true and that 
        player wins. 
        '''
        starting_positions = [(0, 2), (0, 1), (0, 0), (1, 0), (2, 0), (3, 0)]   #when looking at a connect four board the startig positions that would allow for a sequence of 4 matching tiles in a diagnol to the right are found in, starting_positions. 
        for position in starting_positions:         #iterates through the starting positions 
            column, row = position                  #sets the column and row variables to one of the starting positions in the list of starting_positions. 
            counter = 0                             #count of matching tiles in a right diagnol. 
            checkColor = Color.NONE                 #color of tile that we are checking matches for. 
            while(column < 7 and row < 6):          #checks the rest of the spaces in board from our starting positions. 
                tile = self.grid[column][row]       #sets the tile for checking for a match, the right diagnol tiles will be set to this variable for checking for matches. 
                if(tile.color == Color.NONE):       #if empty space is found, skip this position because it cannot create a matching sequence from this position. 
                    break

                if(checkColor == Color.NONE):       #if the tile is empty then we reset the counter to 1.
                    counter = 1
                elif(checkColor == tile.color):     #if a matching tile is cound add 1 to our matching tile count. 
                    counter += 1
                else:                               #if another color is found, then start our count at 1 and switch colors to see if a connect four is present in the rest of the diagnol with the other color. 
                    counter = 1
                checkColor = tile.color

                if(counter == 4):                   # returns true if a player has a matching four tiles in the right diagnol space of a position in our board. 
                    return True
                
                column += 1                         #to check the right diagnol spaces of a sarting position we will need to add 1 to the column and row of the start positition. 
                row += 1
        return False                

    def checkLeftDiagonals(self):
        '''
        Checks if the Board has four tiles of the same color in a Left Diagnol. If found returns true and that 
        player wins.
        '''
        starting_positions = [(6, 2), (6, 1), (6, 0), (5, 0), (4, 0), (3, 0)]  #when looking at a connect four board the startig positions that would allow for a sequence of 4 matching tiles in a diagnol to the left are found in, starting_positions. 
        for position in starting_positions:     #iterates through the starting positions 
            column, row = position                  #sets the column and row variables to one of the starting positions in the list of starting_positions. 
            counter = 0                             #count of matching tiles in a right diagnol. 
            checkColor = Color.NONE                 #color of tile that we are checking matches for. 
           
           #! consider making this while loop 0 and row>6 ,we are starting from left posiitons, the columns are decreased presumably at the end, and the last row is the top left one (0,6)
            while(column < 7 and row < 6):          # The while loop moves through the board until we get to a position that is 
                tile = self.grid[column][row]       # off the board from our starting positions. The function checks for empty spaces and resets the count to one if found.
                if(tile.color == Color.NONE):       #the function also counts the number of matching tiles in a left diagnol, resetting the count and swapping color checked for if another tile color is found. 
                    break                           # this checks the remaining part of that diagnol sequence for a matching left diagnal when another tiles color is found but have not reached the end of the board.  

                if(checkColor == Color.NONE):
                    counter = 1
                elif(checkColor == tile.color):
                    counter += 1
                else:
                    counter = 1
                checkColor = tile.color

                if(counter == 4):
                    return True
                
                column -= 1  #! the while loop checks that column/row is less than 7, these will create infinite loop bc we are decreasing each time
                row += 1 
        return False
