import pandas as pd
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler,MinMaxScaler


df = sns.load_dataset('titanic')
df2 = df[['survived','pclass','age','parch']]
# print(df2.head())
df3 = df2.fillna(df2.mean())

x = df3.drop('survived', axis=1)
y = df3['survived']
# print(x.shape, y.shape)

x_train , x_test , y_train,y_test = train_test_split(x,y,test_size=0.2, random_state=51)
'''The data is split into training and testing sets using the train_test_split function. 80% of the data is used for 
    training (x_train, y_train), and 20% is used for testing (x_test, y_test).
'''
# print(x_train.shape, x_test.shape,y_train.shape,y_train.shape)

sc = StandardScaler()
sc.fit(x_train)
# print(x_train.describe())
x_train_sc = sc.transform(x_train)
x_test_sc = sc.transform(x_test)

pd.set_option('display.float_format', '{:.2f}'.format)
x_train_sc = pd.DataFrame(x_train_sc,columns=['pclass','age','parch'])
x_test_sc = pd.DataFrame(x_test_sc,columns=['pclass','age','parch'])
# print(x_train_sc.describe())


mmc = MinMaxScaler()
mmc.fit(x_train)
# print(x_train.describe())
x_train_mmc = mmc.transform(x_train)
x_test_mmc = mmc.transform(x_test)

x_train_mmc = pd.DataFrame(x_train_mmc,columns=['pclass','age','parch'])
x_test_mmc = pd.DataFrame(x_test_mmc,columns=['pclass','age','parch'])
print(x_train_mmc.describe())


'''Use StandardScaler when the distribution of your data is approximately normal and you want to standardize features.
Use MinMaxScaler when you have reason to believe the distribution is not normal, or when you want features to be on a 
specific scale, especially if your algorithm is sensitive to the scale of input features.
'''