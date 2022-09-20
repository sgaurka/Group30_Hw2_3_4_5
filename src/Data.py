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
     
    def stats(self, places, showCols=self.cols.y, fun="mid"):
        t={}
        for col in showCols:
            v=fun(col)
            if type(v)==int or type(v)==float:
                v=round(v,places)
            t[col.name]=v
        return t
            
     
if __name__ == '__main__':
    data = Data("./../data/auto93.csv")
    print(data)
        
