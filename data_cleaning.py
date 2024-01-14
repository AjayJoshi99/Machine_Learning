import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

'''Deleting row with null values'''
df = pd.read_csv("C:\\Users\\Joshi Ajay\\Downloads\\train.csv")
# print(df)#it will not show all column and rows
pd.set_option('display.max_columns',None)
pd.set_option('display.max_rows',None)
# print(df)#now it will show all records
# print(df.info())# it will print how many values in one column is not null
# print(df.isnull().sum())# counts null values in one column
# sns.heatmap(df.isnull())
# show()

# print(df.isnull().sum()/df.shape[0]*100)#it will show null values in percentage
null_var = df.isnull().sum()/df.shape[0]*100 #it returns key (column) and value(percentage)
drop_var = null_var[null_var > 17].keys()
# print(drop_var)

df3 = df.drop(columns= drop_var)#removing column with morethan 17% null values
# print(df3.shape)


# sns.heatmap(df3.isnull())
# show()


df4 = df3.dropna()#removes all rows which contains at least one null value
# print(df4.shape)

# sns.heatmap(df4.isnull())
# show()

'''Comparing original dataset to cleaned dataset'''

# print(df4.select_dtypes(include=['int64','float64']).columns)
# plt.figure(figsize=(25,25))
# for i, var in enumerate(['MSSubClass', 'LotArea', 'OverallQual', 'OverallCond',
#        'YearBuilt', 'YearRemodAdd', 'MasVnrArea', 'BsmtFinSF1', 'BsmtFinSF2',
#        'BsmtUnfSF', 'TotalBsmtSF', '1stFlrSF', '2ndFlrSF', 'LowQualFinSF',
#        'GrLivArea', 'BsmtFullBath', 'BsmtHalfBath', 'FullBath', 'HalfBath',
#        'BedroomAbvGr', 'KitchenAbvGr', 'TotRmsAbvGrd', 'Fireplaces',
#        'GarageYrBlt', 'GarageCars', 'GarageArea', 'WoodDeckSF', 'OpenPorchSF',
#        'EnclosedPorch', '3SsnPorch', 'ScreenPorch', 'PoolArea', 'MiscVal',
#        'MoSold', 'YrSold', 'SalePrice']):
#     plt.subplot(9,4,i+1)
#     sns.histplot(df[var])
#     sns.histplot(df4[var])
# plt.show()


#cheking one value before and after cleaning
# print(pd.concat([df['MSSubClass'].value_counts()/df.shape[0]*100,
#            df4['MSSubClass'].value_counts()/df4.shape[0]*100 ],
#           keys=['old', 'new'], axis=1)
#       )
