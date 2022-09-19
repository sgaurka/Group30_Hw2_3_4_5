from csv_parser import csv
from Cols import Cols
from Row import Row

class Data:
    
    def __init__(self, src):
        self.src = src
        self.cols = None
        self.rows = {}
        
    def create(self):
       csv(self.src, self.add)
       
    def add(self, xs):
        if len(self.cols) == 0:
            self.cols = Cols(xs)
        else:
            try:
                self.rows.append(xs.cells)
            except:
                self.rows.append(Row(xs))
            row=self.rows
            for todo in self.cols.x+self.cols.y:
                for col in todo:
                    col.add(row.cells[col.at])
            
     
if __name__ == '__main__':
    data = Data("./../data/auto93.csv")
    print(data)
        
