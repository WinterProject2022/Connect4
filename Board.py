from Color import Color
from Tile import Tile

class Board(object):
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

        for column in range(len(self.grid)):
            for row in range(6):
                self.grid[column].append(Tile(Color.NONE, column, row))

    def dropTile(self, column, color):
        for tile in self.grid[column]:
            if(tile.color == Color.NONE):
                tile.color = color
                return True
        return False

    def checkColumns(self):
        for column in self.grid:
            counter = 0
            checkColor = Color.NONE
            for tile in column:
                if(tile.color == Color.NONE):
                    break

                if(checkColor == Color.NONE):
                    counter = 1
                elif(checkColor == tile.color):
                    counter += 1
                else:
                    counter = 1
                checkColor = tile.color

                if(counter == 4):
                    return True
        return False

    def checkRows(self):
        for row in range(6):
            counter = 0
            checkColor = Color.NONE
            for column in self.grid:
                tile = column[row]
                if(tile.color == Color.NONE):
                    break

                if(checkColor == Color.NONE):
                    counter = 1
                elif(checkColor == tile.color):
                    counter += 1
                else:
                    counter = 1
                checkColor = tile.color

                if(counter == 4):
                    return True

    def checkRightDiagonals(self):
        starting_positions = [(0, 2), (0, 1), (0, 0), (1, 0), (2, 0), (3, 0)]
        for position in starting_positions:
            column, row = position
            counter = 0
            checkColor = Color.NONE
            while(column < 7 and row < 6):
                tile = self.grid[column][row]
                if(tile.color == Color.NONE):
                    break

                if(checkColor == Color.NONE):
                    counter = 1
                elif(checkColor == tile.color):
                    counter += 1
                else:
                    counter = 1
                checkColor = tile.color

                if(counter == 4):
                    return True
                
                column += 1
                row += 1
        return False

    def checkLeftDiagonals(self):
        starting_positions = [(6, 2), (6, 1), (6, 0), (5, 0), (4, 0), (3, 0)]
        for position in starting_positions:
            column, row = position
            counter = 0
            checkColor = Color.NONE
            while(column < 7 and row < 6):
                tile = self.grid[column][row]
                if(tile.color == Color.NONE):
                    break

                if(checkColor == Color.NONE):
                    counter = 1
                elif(checkColor == tile.color):
                    counter += 1
                else:
                    counter = 1
                checkColor = tile.color

                if(counter == 4):
                    return True
                
                column -= 1
                row += 1
        return False
