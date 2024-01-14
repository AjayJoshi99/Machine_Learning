import pandas as pd
import seaborn as sns
from sklearn.preprocessing import OneHotEncoder

tips = sns.load_dataset("tips")
pd.set_option('display.max_columns',None)

# print(tips.columns)
# dummy_df = pd.get_dummies(tips)
# print(dummy_df.columns)'''['total_bill', 'tip', 'size', 'sex_Male', 'sex_Female', 'smoker_Yes',
#        'smoker_No', 'day_Thur', 'day_Fri', 'day_Sat', 'day_Sun', 'time_Lunch',
#        'time_Dinner']'''

# dummy_df = pd.get_dummies(tips,drop_first=True)
# print(dummy_df.columns)'''['total_bill', 'tip', 'size', 'sex_Female', 'smoker_No', 'day_Fri',
#        'day_Sat', 'day_Sun', 'time_Dinner']'''

'''In One-Hot Encoding, each category is represented as a binary vector. Each category is mapped to a vector of length 
    equal to the number of categories, with a 1 at the index corresponding to the category and 0 elsewhere.
'''
obj = OneHotEncoder(sparse_output=False)
new_df = obj.fit_transform(tips[['sex','smoker','day','time']])
# print(new_df.dtype)
df2 = pd.DataFrame(new_df, columns=[ 'sex_Male', 'sex_Female', 'smoker_Yes',
       'smoker_No', 'day_Thur', 'day_Fri', 'day_Sat', 'day_Sun', 'time_Lunch',
       'time_Dinner'])
print(df2.head())