import random
import sys
sys.path.append('src')
from csv_parser import cli, the, csv
from numeric import Num
from Sym import Sym
from Data import Data
from Row import Row
from Cols import Cols

## Test Engine
eg, fails = {}, 0
## 1. reset random number seed before running something.
## 2. Cache the detaults settings, and...
## 3. ... restore them after the test
## 4. Print error messages or stack dumps as required.
## 5. Return true if this all went well.
def runs(k):
    if not eg.get(k):
        return
    random.seed(the['seed'])
    old ={}
    num = 0
    for i in the:
        old[num] = i
        num = num + 1
    if the['dump']:
        status,out = True, eg[k]()
    else:
        try:
            status,out = True, eg[k]()
        except:
            status, out = False, False
    for i, v in enumerate(old):
        the[i] = v
    msg = status and ((out == True and "PASS") or "FAIL") or "CRASH"
    # print(status, out, k, msg, out)
    print("!!!!!!", msg, k , status)
    return out

def run_all_tests():
    fails = 0
    for _, value in enumerate(eg):
        print("\n-----------------------------------")
        if not runs(value):
            fails = fails + 1
        print("Fails: ", fails)

def eg_the():
    if the:
        print('\n', the)
        return True
    else:
        print('the does not exist')
        return False
eg['the'] = eg_the

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
    
    print(mode, entropy)
    return mode == "a" and 1.37 <= entropy and entropy <= 1.38   
eg['sym'] = eg_sym

## The middle and diversity of a set of numbers is called "median" 
## and "standard deviation" (and the latter is zero when all the nums 
## are the same).
def eg_num():
    num = Num(0,"")
    for i in range(1,100):
        num.add(i,float('inf'))
    mid = num.mid()
    div = num.div()
    print('mid: {}, div: {}'.format(mid, div))
    return mid >= 50 and mid <= 52 and div > 30.5 and div < 32
eg['num'] = eg_num

## Nums store only a sample of the numbers added to it (and that storage 
## is done such that the kept numbers span the range of inputs).
def eg_bignum():
    num=Num(0, '')
    for x in range(1, 1000):
        num.add(x, 32)
    num._has.sort()
    print(num._has)
    return len(num._has) == 32
eg['bignum'] = eg_bignum

## Show we can read csv files.
def eg_csv():
    n = 0
    if n < 10:
        csv("./data/auto93.csv", print)
        n += 1
    return True
eg['csv'] = eg_csv
        
## Can I load a csv file into a Data?.
def eg_data():
    d = Data("./data/auto93.csv")
    for _, col in enumerate(d.cols.y):
        print(col)
    return True
eg['data'] = eg_data

## Print some stats on columns.
def eg_stats():
    data = Data("./data/auto93.csv")
    div = lambda col: col.div
    mid = lambda col: col.mid
    print('-----------------------------------')
    print("xmid", data.stats(2,data.cols.x, mid))
    print("xdiv", data.stats(3,data.cols.x, div))
    print("ymid", data.stats(2,data.cols.y, mid))
    print("ydiv", data.stats(3,data.cols.y, div))
    return True
eg['stats'] = eg_stats


if __name__ == "__main__":
    args = sys.argv
    the = cli(the, args)
    run_all_tests()
    
