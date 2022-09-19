import re
from Sym import Sym
from numeric import Num
from csv_parser import push

class Cols:
    def __init__(self,names=""):
      self.names=names
      self.all=[]
      self.klass=None
      self.x=[]
      self.y=[]

      for c, s in names.items():
        if re.search("^[A-Z]",s)!=None:
          col=push(self.all, Num(c,s))
          col= push(self.all, Sym(c,s))
        if re.search(":$",s)==None:
          if re.search("[!+=]",s)!=None:
            push(self.y,col)
          else:
            push(self.x,col)
          if re.search("!$",s)!=None:
            self.klass=col

if __name__ == '__main__':
    cols = Cols('Clndrs','Volume','Hp:','Lbs-','Acc+','Model','origin','Mpg+')
  
