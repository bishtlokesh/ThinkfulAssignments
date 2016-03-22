import matplotlib.pyplot as py
import pandas as pn
import numpy as np
import scipy.stats as stats
import collections as col

def main():
    loansData=pn.read_csv('https://github.com/Thinkful-Ed/curric-data-001-data-sets/raw/master/loans/loansData.csv')
    loansData2=preProcess(loansData)
    cnt=col.Counter(loansData2['Open.CREDIT.Lines'])
    for key, val in cnt.items():
        print("key: {}"  "value: {}"  .format(key, val))
    py.bar(cnt.keys(), cnt.values(), 1)
    py.show()
    #stats.chisquare(cnt.values())
    chi, p = stats.chisquare(cnt.values())
    #print(chi,p)
    print(cnt)
    


def preProcess(Data):
    Data2=Data.dropna(inplace=False)
    return Data2
if __name__=="__main__": main()