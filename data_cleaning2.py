import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

'''Filling null values with mean, only for numeric data'''

df = pd.read_csv("C:\\Users\\Joshi Ajay\\Downloads\\train.csv")
pd.set_option('display.max_rows',None)
pd.set_option('display.max_columns',None)

null_var = df.isnull().sum()/df.shape[0]*100
remove_var=null_var[null_var>20].keys()
df2 = df.drop(columns=remove_var)

df2 = df2.select_dtypes(include=['int64','float64'])
# print(remove_var)
missing_val = [var for var in df2.columns if df2[var].isnull().sum()>0 ]
# print(missing_val)
df3 = df2.fillna(df2.mean())
# print(df3.isnull().sum().sum())

# plt.figure(figsize=(10,10))
# sns.set()
# for i,var in enumerate(missing_val):
#     plt.subplot(2,2,i+1)
#     sns.histplot(df2[var], label='old')
#     sns.histplot(df3[var], label='new')
#     plt.legend()
# plt.show()

df_concat = pd.concat([df2[missing_val],df3[missing_val]],axis=1)
print(df_concat[df_concat.isnull().any(axis=1)])