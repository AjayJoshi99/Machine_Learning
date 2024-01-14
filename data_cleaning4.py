import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("C:\\Users\\Joshi Ajay\\Downloads\\train.csv")
df2 = df.select_dtypes(include=['object'])
null_var = df2.isnull().mean()*100 #it will return column name and percentage
missing_var = null_var[null_var>0].keys()
for var in missing_var:
    df2[var].fillna(df2[var].mode()[0], inplace=True)
    # print(var , "==>>",df2[var].mode()[0])

# print(df2.isnull().sum().sum()) # only null values in object will be filled
# df3 = df.select_dtypes(include=['object'])
# df4 = df.select_dtypes(include=['int64','float64'])
# print(df.shape)# total rows and column (1460, 81)
# print(df3.shape)# rows and column only with objects  (1460, 43)
# print(df4.shape)# rows and column only with int and float (1460, 38)


# plt.figure(figsize=(16,9))
# for i, var in enumerate(missing_var):
#     plt.subplot(4,4,i+1)
#     plt.hist(df[var].dropna(), label='old')
#     plt.hist(df2[var], label='new')
# plt.show()
