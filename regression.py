import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler,PolynomialFeatures
from sklearn.linear_model import LinearRegression,Ridge, Lasso
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score

pd.set_option("display.max_columns",None)
pd.set_option('display.width', False)# disable wrapping of DataFrame display.
df = pd.read_csv(r"C:\Users\Joshi Ajay\Downloads\bangalore house price prediction OHE-data.csv")
# print(df.head(1))

x = df.drop('price',axis=1)
y = df['price']
# print(x.shape, y.shape)

x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2, random_state=51)
sc = StandardScaler()
sc.fit(x_train)
sc.fit(x_test)

x_train = sc.transform(x_train)
x_test = sc.transform(x_test)

'''LinearRegression'''
lr = LinearRegression()
lr.fit(x_train,y_train)

y_pred = lr.predict(x_test)
print(lr.predict([x_test[0,:]]))#[76.90661876]
# # print(lr.predict(x_test),'\n',y_test)#comparison
# print(lr.score(x_test,y_test))#accurecy - 0.7903837092682249

'''RidgeRegression'''
# rd = Ridge()
# rd.fit(x_train, y_train)
# print(rd.score(x_test,y_test))#accurecy - 0.790983427490572

'''LassoRegression'''
# ls = Lasso(alpha=6)
# ls.fit(x_train, y_train)
# print(ls.score(x_test,y_test))
#accurecy - 0.8125012107833113  for alpha = 1
#           0.8387532822359542  for alpha = 3
#           0.843024833779153   for alpha = 6


# mse = mean_squared_error(y_test, y_pred)
# rmse = np.sqrt(mse)
# print(rmse)#64.89843531105612

'''R2=0 indicates that the model does not explain any of the variability in the target variable.
   R2=1 indicates that the model perfectly explains the variability in the target variable.
'''
# print(r2_score(y_test, y_pred))#0.7903837092682249

'''In machine learning, PolynomialFeatures is a feature engineering technique used to generate polynomial features 
   from the original features of a dataset. 
    
    The idea behind PolynomialFeatures is to create new features by raising the existing features to different powers 
    and also considering interactions between different features.
    
    PolynomialFeatures is commonly used in combination with linear regression or other regression algorithms to capture 
    non-linear relationships between features and the target variable. It allows the model to learn more complex 
    patterns in the data.    
'''

# poly_reg = PolynomialFeatures(degree=2)
# poly_reg.fit(x_train)
# x_train_poly = poly_reg.transform(x_train)
# x_test_poly = poly_reg.transform(x_test)

# lr = LinearRegression()
# lr.fit(x_train_poly,y_train)
#
# print(lr.score(x_test_poly,y_test))#0.997293410146066


