class Tile(object):
    '''
    Referes to a specific square in our board that will be both the board and the player pieces.
    Represented as one of the  3 color choices: Red, Yellow, None(White)
    '''
    def __init__(self, color, column, row):
        '''
        Constructor for our Tile
        :param color: This is the color of the Tile. (RED,YELLOW,NONE)
        :param column: This is the column of the Tile.(0-7)
        :param row: This is the row of the Tile.(0-6) 
        '''
        self.color = color
        self.column = column
        self.row = row

    def __str__(self):
        '''
        The ToString method that returns an individual Tiles color and position . 
        '''
        return "Color: " + str(self.color.name) + "\tColumn: " + str(self.column) + "\tRow: " + str(self.row)