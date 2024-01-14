import pandas as pd
import seaborn as sns
import numpy as np
from sklearn.impute import SimpleImputer

test = pd.read_csv(r"C:\Users\Joshi Ajay\Downloads\test.csv")
train = pd.read_csv("C:\\Users\\Joshi Ajay\\Downloads\\train.csv")
# print(test.shape)#(1459, 80)
# print(train.shape)#(1460, 81)
x_train = train.drop(columns='SalePrice')
y_train = train['SalePrice']

'''
    x_train: This represents the set of features or independent variables in your training dataset. 
    These are the variables that you use to predict the target variable.

    y_train: This represents the target variable or the dependent variable in your training dataset. 
    In this case, it is the 'SalePrice' column. The model you are building will try to predict the values 
    in this column based on the features in x_train.
'''

num_val = x_train.select_dtypes(include=['int64','float64']).columns
cat_val = x_train.select_dtypes(include=['O']).columns
# print(num_val)
imputer_mean = SimpleImputer(strategy='mean') #defining what will replace null value
imputer_mode = SimpleImputer(strategy='most_frequent')

imputer_mean.fit(x_train[num_val])#calculating replacement of null value
imputer_mode.fit(x_train[cat_val])

# print(imputer_mean.transform(x_train[num_val])) 2d array
x_train[num_val] = imputer_mean.transform(x_train[num_val])#replacing null values
test[num_val] = imputer_mean.transform(test[num_val])
x_train[cat_val] = imputer_mode.transform(x_train[cat_val])
test[cat_val] = imputer_mode.transform(test[cat_val])
print(x_train)

