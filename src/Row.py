import math
import copy from csv_parser


class Row:
    cells = {}
    cooked = {}
    isEvaled = False

    def __init__(self, t):
        if t:
            self.cells = t
        self.cooked = Row.copy(t)
        self.isEvaled = False
       
if __name__ == '__main__':
    row = Row({2:3})
    
