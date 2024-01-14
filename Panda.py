import pandas as pd
'''Series has more efficiency than list when working with tabular data'''
# print(pd.__version__)
# sr1 = pd.Series([12,-90,'AJAY','@3',987.19])
# sr2 = pd.Series([12,-90,'AJAY','@3',987.19],index=['a','b','c','d','e'], name="Practice")
# sr3 = pd.Series({'a':12, 'b':-90, 'c':'AJAY', 'd':'@3', 'c': 987.19})
# sr4 = pd.Series([1,2,3,4,5])
# sr5 = pd.Series([6,7,8,9,10])
# sr4+sr5 do sum of series's value
'''DataFrames contains label access thorugh both row index and column index'''
# df1 = pd.DataFrame({'id': [1,2,3,4],'Name':['Ajay','Het','Jay','Devraj']})
# df2 = pd.DataFrame([{'a':12, 'b':-90, 'c':'AJAY', 'd':'@3', 'c': 987.19} ,{'a':24, 'b':-180, 'c':'JOSHI', 'd':'#4', 'c': 1892.09}])
# df3 = pd.read_csv("C:\\Users\\Joshi Ajay\\Documents\\Pandas_practice1.csv")
# df3.columns  --->Index(['Student', 'Gender', 'Score', 'Pass/Fail', 'Letter', 'Outlier','Award'],dtype='object')
# df4 = pd.read_csv("C:\\Users\\Joshi Ajay\\Documents\\Pandas_practice1.csv",nrows = 4)
# df5 = pd.read_csv("C:\\Users\\Joshi Ajay\\Documents\\Pandas_practice1.csv",usecols = [1,2,4])--> prints all rows with desired column
# df6 = pd.read_csv("C:\\Users\\Joshi Ajay\\Documents\\Pandas_practice1.csv", skiprows= 10)
# df6 = pd.read_csv("C:\\Users\\Joshi Ajay\\Documents\\Pandas_practice1.csv", skiprows= [16]) skips given rows only
# df7 = pd.read_csv("C:\\Users\\Joshi Ajay\\Documents\\Pandas_practice1.csv",skiprows= [16], index_col='Student')
# df8 = pd.read_csv("C:\\Users\\Joshi Ajay\\Documents\\Pandas_practice1.csv", skiprows= [16], header= 0) #0th index will be header
# df9 = pd.read_csv("C:\\Users\\Joshi Ajay\\Documents\\Pandas_practice1.csv", names =['A','B','C','D','E','F','G']) --> provides column index
# df9.head()--> it will show first 5 rows
# df9.head(10) --> for first 10 rows
# df9.tail() --> it will show last 5 rows
#df9.tail(10)--> for last 10 rows
# df10 = pd.read_csv("C:\\Users\\Joshi Ajay\\Documents\\Pandas_practice1.csv", dtype={'Score': 'float64'})
# df11 = pd.read_csv("C:\\Users\\Joshi Ajay\\Documents\\Pandas_practice1.csv", keep_default_na=False)
# df12 = pd.read_csv("C:\\Users\\Joshi Ajay\\Documents\\Pandas_practice1.csv", na_filter=False) --> it will not fill null value with NAN
# isnull() --> returns data in form of true and flase
# df12.isnull().sum() --> returns how many values are null in a raw
# df12.isnull().sum().sum() --> returns how many values are null in a data file
# df12 = pd.read_csv("C:\\Users\\Joshi Ajay\\Documents\\Pandas_practice1.csv")
# df12.dropna() --> shows only rows which does not contain Null value
# df12.dropna(axis=1)--> shows only rows which does not contain Null value
# df12.dropna(how = 'all') --> removes only rows which is completely filed with null
# df12.dropna(how = 'any') --> removes only rows which have atleast one  null values.
# df12.dropna(thresh = 1) --> rows with fewer null values will be dropped
# df12.dropna(subset = ['Student']) -->removes only rows which have atleast one  null value in given colunm.
# df12.dropna(inplace = False) --> default value
#df12.dropna(inplace = True) --> it make changes in original data frame.
#df12.fillna(0)--> fill all null values with given values
#df12.fillna({'Student':'Unknown', 'Score': 0, 'Letter' : 'x'})
#df12.fillna(method = 'bfill')--> fills null with backward values from raws
#df12.fillna(method = 'ffill')--> fills null with forward values from raws
#df12.fillna(method = 'ffill', axis = 1) --> fills null with forward values from colunm
#df12.fillna('hi', limit =1 ) --> fills only given number of null values to given values
# df12.replace('Alan','Ajay')
# df12.replace({'Value' : 11}, 12)
# df12.replace('Sally', method = 'ffill')
# df12.replace([11,10,13,48],[61,60,63,98], inplace=True
# print(df12)

# df12 = pd.read_csv("C:\\Users\\Joshi Ajay\\Documents\\Pandas_practice1.csv")
#df12.interpolate()--> it will fill numeric null values
#type(df12.Date[0]) --> return type of date
#df12.interpolate(method='index') --> it will fill numeric value according to index
#df12.interpolate(method='polynomial', order= 2)
#df12.interpolate(method='nearest')
# df12.interpolate(limit=2)
# df12.interpolate(limit=2, limit_direction='forward')
# df12.interpolate(inplace=True)
# loc = Location
#df12.loc[0] --> prints 0th row
# df12.loc[[1,4]]
# df12.loc[4,'Student'] --> return perticular value
# df12.loc[0:4,'Student']-->return perticular value in given range
# df12.loc[df12['Value']<50]
# df12.iloc[0]--> prints 0th colunm
# df12.iloc[:,2]
'''ONLY DIFFERENCE BETWEEN ILOC AND LOC IS THAT IN ILOC WE CAN USE ONLY ACTUAL INDEX TO RETRIVE COLUNM.'''
# df12.groupby(by='Gender').groups --> returns index of group elements.
# df12.groupby('Gender').groups --> returns index of group elements.
# df12.groupby(['Gender','Outlier']).groups
# df13 = df12.groupby('Gender').get_group('M') -->returns all data of male
# for i, j in df12.groupby(['Gender','Outlier']): --> prints data in groups
#     print(i,j)
# df13 = df12.loc[:,['Value','Score']]
# df13.sum()--> do sum of all colunm
# df13.descibe() --> it returns min, 25%,50%,75%,max, count,mean . if all rows contain int only
# df13.agg(['sum','max','min','mean'])

# df1 = pd.DataFrame({'id': [1,2,3,4],'Name':['Ajay','Het','Jay','Devraj']})
# df2 = pd.DataFrame({'id': [1,2,3,4,5],'Sname':['Joshi','Dalasaniya','Nasit','Gohil','Jivani']})
# df3 = pd.merge(df1,df2)
# df3 = pd.merge(df1,df2,  on ='id')
# df3 = pd.merge(df1,df2 , how ='right') --> left, right,outer joins
# df3 = pd.merge(df1,df2 , how ='right', indicator=True)--> it will add a colunm which discribes join type
# df1 = pd.DataFrame({'id': [1,2,3,4],'Name':['Ajay','Het','Jay','Devraj']})
# df2 = pd.DataFrame({'id': [1,2,3,4,5],'Name':['Joshi','Dalasaniya','Nasit','Gohil','Jivani']})
# df3 = pd.merge(df1,df2, left_index=True, right_index=True)-->it is used when both dataframe contains same name
# df3 = pd.merge(df1,df2,on='id', suffixes=('_First','_Last'))
# print(df3)
# sr4 = pd.Series([1,2,3,4,5,6,7,8,9])
# sr5 = pd.Series([6,7,8,9,10],)
# pd.concat([sr4,sr5],axis=1,ignore_index=True)
# pd.concat([sr4,sr5],axis = 1,join = 'outer') only innner and outer joins
# df1 = pd.DataFrame({'id': [1,2,3,4],'Name':[10,20,30,40]})
# df2 = pd.DataFrame({'id': [1,2,3,4],'Sname':[50,60,70,80]})
# pd.concat([df1,df2],axis =1, keys =['df1','df2'])
# df1.join(df2, lsuffix='_1',rsuffix='_2') similar with merge
# df1._append(df2)
# df1._append(df2, ignore_index=True)
# df12 = pd.read_csv("C:\\Users\\Joshi Ajay\\Documents\\Pandas_practice1.csv")
# df12.pivot_table(index='Value',aggfunc='max')
# pd.pivot_table(df12,index='Value',columns='Gender',fill_value='Hi',aggfunc='sum')
# pd.melt(df12)-->all possible combinations
# pd.melt(df12, id_vars='Gender')
# pd.melt(df12, id_vars='Gender',value_vars='Score')
# print(pd.melt(df12, id_vars='Gender',value_vars='Score'))
