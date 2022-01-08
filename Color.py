from enum import Enum

class Color(Enum):
    '''
    This is our constructor for setting the color of our connect four pieces. 
    :param RED: Red is value 1.
    :param YELLOW Yellow is value -1.
    :param NONE: used to indicate a empty Tile in our Board; value 0. 
    '''
    RED = 1
    YELLOW = -1
    NONE = 0