import math
import copy from csv_parser

class Row:
    cells = {}
    cooked = 0
    isEvaled = false

    def __init__(self, t):
        if t:
            self.cells = t
        self.cooked = copy(t)
        self.isEvaled = false
       
    if __name__ == '__main__':
        row = Row(t={2:3,4:5})
        
