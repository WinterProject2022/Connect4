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