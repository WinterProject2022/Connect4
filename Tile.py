class Tile(object):
    def __init__(self, color, column, row):
        self.color = color
        self.column = column
        self.row = row

    def __str__(self):
        return "Color: " + str(self.color.name) + "\tColumn: " + str(self.column) + "\tRow: " + str(self.row)