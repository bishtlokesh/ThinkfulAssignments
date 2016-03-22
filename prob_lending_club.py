import matplotlib.pyplot as py
import pandas as pn
from unittest.mock import inplace
from sympy.combinatorics.subsets import Subset
import scipy.stats as stats

def main():
    loansData=pn.read_csv('https://github.com/Thinkful-Ed/curric-data-001-data-sets/raw/master/loans/loansData.csv')
    #print(loansData[1:5])
    #writeFile(loansData)
    loansData2=preProcess(loansData)

#check for NA values, missing values outliers
def writeFile(data):
    fout=open("loansData.txt", 'w')
    data.to_csv('LoansData2.csv')

def preProcess(Data):
    Data.dropna(inplace=True)

   # print(Data[:3])
   # data_sub=Data['Amount.Funded.By.Investors']
    #print(data_sub)
    #py.boxplot(data_sub)
    Data.boxplot(column='Amount.Requested')
   # py.show()
    Data.hist(column='Amount.Requested')
   # Data.qq(column='Amount.Funded.By.Investors')
    py.show()
    stats.probplot(Data['Amount.Requested'], dist='norm', plot=py)
    py.show()
    return Data
           
if __name__=='__main__': main()
