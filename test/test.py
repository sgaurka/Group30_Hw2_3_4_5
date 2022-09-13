import random
import sys
sys.path.append('src')
from csv_parser import the
from numeric import Num
from Sym import Sym

## Test Engine
eg, fails = {}, 0
## 1. reset random number seed before running something.
## 2. Cache the detaults settings, and...
## 3. ... restore them after the test
## 4. Print error messages or stack dumps as required.
## 5. Return true if this all went well.
def runs(k,old,status,out,msg):
    the = Num.the
    if not eg[k]:
        return
    random.seed(the.seed)
    old ={}
    num = 0
    for i in the:
        old[num] = i
        num = num + 1
    if the.dump:
        status,out = True, eg[k]
    else:
        try:
            status,out = True, eg[k]
        except:
            out = "Exception thrown. eg does not exist."
    num = 0
    for j in old:
        the[num] = j
        num = num + 1
    msg = status and ((out == TRUE and "PASS") or "FAIL") or "CRASH"
    print("!!!!!!", msg, k , status)
    return out

def eg_the():
    print(the)

## The middle and diversity of a set of symbols is called "mode" 
## and "entropy" (and the latter is zero when all the symbols 
## are the same).
def eg_sym():
    sym = Sym(0,"")
    for x in ["a","a","a","a","b","b","c"]:
        sym.add(x)
    mode, entropy = sym.mid(), sym.div()
    entropy = (1000*entropy.real)//1/1000
    print('mid: {}, div: {}'.format(mode, entropy))
    
    if not (mode=="a" and 1.37 <= entropy and entropy <= 1.38):
        raise AssertionError()
    else:
        print("Sym test passed")


## The middle and diversity of a set of numbers is called "median" 
## and "standard deviation" (and the latter is zero when all the nums 
## are the same).
def eg_num():
    print('\n-----------------------------------')
    num = Num(0,"")
    for i in range(1,100):
        num.add(i,float('inf'))
    mid = num.mid()
    div = num.div()
    print('mid: {}, div: {}'.format(mid, div))
    if not (mid >= 50 and mid <= 52 and div > 30.5 and div <32):
        raise AssertionError()
    else:
        print("Num test passed")

## Nums store only a sample of the numbers added to it (and that storage 
## is done such that the kept numbers span the range of inputs).
def eg_bignum():
    print('\n-----------------------------------')
    num=Num(0, '')
    for x in range(1, 1000):
        num.add(x, 32)
    num._has.sort()
    print(num._has)
    print('Passed? =', len(num._has) == 32)
    
## Show we can read csv files.
def eg_csv():
        n=0
        csv= Data("../data/source.csv")
        row()
        n = n+1
        if n>10:
            return
        else:
            Num.print_Csv() 
        
## Can I load a csv file into a Data?.
def eg_data(data):
    d = Data("../data/source.csv")
    print('-----------------------------------')
    for c in d.col.y:
        print(d.data(c))
    assert True

## Print some stats on columns.
def eg_stats():
    data = Data("../data/source.csv")
    div = Col.div()
    mid = Col.mid()
    print('-----------------------------------')
    print(data.stats(2,data.col.x,"mid"))
    print(data.stats(3,data.col.x,"div"))
    print(data.stats(2,data.col.y,"mid"))
    print(data.stats(3,data.col.y,"div"))
    assert True


if __name__ == "__main__":
    eg_the()
    eg_num()
    eg_sym()
    eg_bignum()
    eg_csv()
    eg_data()
    eg_stats()
    