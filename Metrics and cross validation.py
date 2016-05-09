
# coding: utf-8

# In[98]:

from sklearn.cross_validation import KFold
import numpy as np
kf=KFold(4, n_folds=4)
for train, test in kf:
    print(train)
X = np.array([[0., 0.], [1., 1.], [-1., -1.], [2., 2.]])
y = np.array([0, 1, 0, 1])
X_train, X_test, y_train, y_test = X[train], X[test], y[train], y[test]
print(X_train, y_train)
print(X_test, y_test)
#print(X,y)
#print(kf)


# In[105]:

import pandas as pd
loansData=pd.read_csv("https://github.com/Thinkful-Ed/curric-data-001-data-sets/raw/master/loans/loansData.csv" )
#loans.head(3)
x = loansData['Interest.Rate'][0:5].values[1]
cleanInterestRate = loansData['Interest.Rate'].map(lambda x: round(float(x.rstrip('%')) / 100, 4))
loansData['Interest.Rate'] = cleanInterestRate
loansData['Interest.Rate'][0:5]
cleanLoanLength = loansData['Loan.Length'].map(lambda x: int(x.rstrip(' months')))
cleanFICORange = loansData['FICO.Range'].map(lambda x: x.split('-'))
cleanFICORange = cleanFICORange.map(lambda x: [int(n) for n in x])
cleanFICORange[0:5]
loansData['FICO.Range'] = cleanFICORange
print(loansData['FICO.Range'][0:5].values[0][0])
loansData.head(4)
print(len(loansData))
for i in range(len(loansData)):
    a[i]=loansData['FICO.Range'].values[i][0]

for i in range(len(loansData)):
    loansData['FICO.Range'].values[i]=a[i]
    
#loansData['FICO.Range']=a    


cleanDebtIncomeRatio=loansData['Debt.To.Income.Ratio'].map(lambda x: round(float(x.rstrip('%'))/100,4))
loansData['Debt.To.Income.Ratio']=cleanDebtIncomeRatio
print(loansData.head())


# In[106]:

loansDatamodel=loansData


# In[126]:

y=loansDatamodel['Interest.Rate']
Y=np.matrix(y).transpose()
print(type(Y))


# In[137]:

import statsmodels.api as sm
#x=loansDatamodel['FICO.Range', 'Amount.Funded.By.Investors']
fico=loansDatamodel['FICO.Range']
funded=loansDatamodel['Amount.Funded.By.Investors']
x1=np.matrix(fico).transpose()
x2=np.matrix(funded).transpose()
x=np.column_stack([x1, x2])
X=sm.add_constant(X)
print((X))


# In[155]:

import numpy as np
from sklearn.cross_validation import KFold
from sklearn.linear_model import LinearRegression
regression=LinearRegression()
kf=KFold(n=len(X), n_folds=10)
xval_err=0
for train,test in kf:
    regression.fit(X[train], Y[train])
    p=regression.predict(X[test])
    e=p-Y[test]
    #np.dot(e,t(e))

