import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from scipy.stats import variation


dataset=pd.read_csv(r'Salary_Data.csv')
x=dataset.iloc[:,:-1] #Years of Experience (Independent variable)
y=dataset.iloc[:,-1] #Salary (Dependent variable)


x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=0)
regressor=LinearRegression()
regressor.fit(x_train,y_train)
y_pred=regressor.predict(x_test)

plt.scatter(x_test,y_test,color='red')
plt.plot(x_train,regressor.predict(x_train),color='blue')
plt.title('Salary vs Experience(Test set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()

m_slope=regressor.coef_
c_intercept=regressor.intercept_
y_12=m_slope*12+c_intercept
bias_score=regressor.score(x_train,y_train) #training score
variance_score=regressor.score(x_test,y_test) #testing score
dataset.mean()
dataset['Salary'].mean()
dataset.median()
dataset.mode()
dataset.var()
dataset.std()
variation(dataset.values)
variation(dataset['Salary'])
dataset.corr()
dataset['Salary'].corr(dataset['YearsExperience'])
dataset.skew()
dataset.sem()
dataset['Salary'].skew()

import scipy.stats as stats
dataset.apply(stats.zscore)
#SSR
y_mean=np.mean(y)
SSR=np.sum((y_pred-y_mean)**2)
print(SSR)
#SSE
y=y[0:6]
SSE=np.sum((y-y_pred)**2)
print(SSE)
#sst
mean_total=np.mean(dataset.values)
SST=np.sum((dataset.values-mean_total)**2)
print(SST)
#r2
r_square=1-SSR/SST
print(r_square)
import pickle
filename='linear_regression_model.pkl'
with open(filename,'wb') as file: 
    pickle.dump(regressor,file)
print("Model has been pickled and saved as linear_regression_model.pkl") #entire 50 lines of code is converted to binary file .pkl