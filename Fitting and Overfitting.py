
# coding: utf-8

# In[8]:

from sklearn.linear_model import LinearRegression
clf=LinearRegression()
clf.fit([[1,1],[2,2], [3,3]], [1,2,3])
clf.coef_
clf.predict([4,4])


# In[28]:

import numpy as np
import statsmodels.formula.api as st
import pandas as pd
np.random.seed(414)


# In[40]:

X=np.linspace(1,15, 1000)
y=3*np.sin(X)+np.random.normal(1+X, 0.2, 1000)
train_X, train_Y=X[:700], y[:700]
test_X, test_Y=X[700:], y[700:]
train_df=pd.DataFrame({'X': train_X, 'y':train_Y})
test_df=pd.DataFrame({'X': test_X, 'y':test_Y})
poly_1=st.ols(formula='y ~ X + 1',data=train_df).fit()
poly_1.summary()


# In[45]:

poly_2=st.ols(formula='y~1+X+I(X**2)', data=train_df).fit()
print(poly_2.summary())


# In[46]:

poly_3=st.ols(formula='y~1+X+I(X**2)+I(X**3)', data=train_df).fit()
print(poly_3.summary())

