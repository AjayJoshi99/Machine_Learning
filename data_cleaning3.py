import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("C:\\Users\\Joshi Ajay\\Downloads\\train.csv")
pd.set_option('display.max_rows',None)
pd.set_option('display.max_columns',None)

null_var = df.isnull().sum()/df.shape[0]*100
remove_var=null_var[null_var>20].keys()
df2 = df.drop(columns=remove_var)

df3 = df2.select_dtypes(include=['int64','float64'])
# print(df3.shape)
missing_val = [var for var in df3.columns if df3[var].isnull().sum()>0 ]
# print(missing_val)

df_copy = df2.copy()
num_vars = ['LotFrontage', 'MasVnrArea','GarageYrBlt']
cat_vars= ['LotConfig','Exterior2nd','KitchenQual'] #these are classes accordingly we we fill nan values
for cat, num in zip(cat_vars,num_vars):
    for var in df[cat].unique():
        df_copy.update(df_copy[df_copy[cat] == var][num].replace(np.nan, df[df[cat] == var][num].mean()))
        '''df_copy[df_copy[cat] == var][num]: This part filters the DataFrame df_copy to include only rows where the 
        categorical variable cat is equal to the current category var. It then selects the numerical variable num from 
        these filtered rows. This creates a Series of numerical values for a specific category.'''
        '''df_copy[df_copy[cat] == var][num] :
            here 'df_copy[cat] == var' is condition it will select all "rows" where catagaory is same
            '[num]' is used to take specific num "column".  '''
print(df_copy[missing_val].isnull().sum())






