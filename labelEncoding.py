'''
Label Encoding:

Motivation --> Machine learning algorithms often require numerical input, and many algorithms cannot directly handle
categorical data in its raw form.
Purpose --> Label encoding transforms categorical labels into numerical values. Each unique category is assigned a unique
integer, making it easier for machine learning models to work with the data.Mapping for 'KitchenQual' column

Motivation --> Sometimes, the order or relationship between categories matters, and this information is not inherently
captured by label encoding.
Purpose --> In the 'KitchenQual' column, there is an inherent ordinal relationship among categories
('Ex' > 'Gd' > 'TA' > 'Fa'). The mapping ensures that this order is preserved, and the machine learning model can
understand that higher numerical values correspond to better quality.
'''

import pandas as pd
from sklearn.preprocessing import LabelEncoder
# "  module(library).submodule  "  class

train = pd.read_csv("C:\\Users\\Joshi Ajay\\Downloads\\train.csv")
pd.set_option('display.max_rows',None)

# print(train.columns)
df2 = train[['KitchenQual','BldgType']]
'''The nested brackets are used to create a new DataFrame df2 by selecting specific columns from the original DataFrame 
    train. The inner brackets ['KitchenQual', 'BldgType'] are used to create a list of column names that are being 
    selected,and the outer brackets train[...] are used to perform the column selection operation on the train DataFrame
    '''

le = LabelEncoder()
df3 = le.fit_transform(df2['BldgType'])

df4 = pd.DataFrame(df3, columns=['BldgType'])
'''In this step, the label encoding is applied to the 'BldgType' column of the DataFrame df2. The fit_transform method 
    is used, which fits the encoder to the unique values in the 'BldgType' column and then transforms those values into 
    numerical labels. '''
'''For example, if the unique values in 'BldgType' are ['A', 'B', 'C'], the label encoding might assign 0 to 'A', 
    1 to 'B', and 2 to 'C'. The order is determined by the unique values' order in the column.'''

# print(df4['BldgType'])
train['BldgType'] = df4['BldgType']
print(train['BldgType'])
'''BldgType
1Fam      1220
TwnhsE     114
Duplex      52
Twnhs       43
2fmCon      31
'''

# order_label = {'Ex':4,'Gd':3,'TA':2,'Fa':1}
# df2['KitchenQual_column_name'] = df2['KitchenQual'].map(order_label)
# # print(df2)


