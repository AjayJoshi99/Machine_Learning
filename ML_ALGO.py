import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
# from sklearn.tree import DecisionTreeRegressor
# from sklearn.ensemble import RandomForestRegressor
# from sklearn.neighbors import KNeighborsRegressor

# import pickle

from sklearn.naive_bayes import GaussianNB, MultinomialNB,BernoulliNB
df = pd.read_csv(r"C:\Users\Joshi Ajay\Downloads\bangalore house price prediction OHE-data.csv")
x = df.drop('price',axis=1)
y = df['price']

x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2, random_state=51)

# print(x_train.head())

'''Decision trees are suitable when the relationships in your data are relatively simple, and you want a model that is 
    easy to interpret.'''
# classifier = DecisionTreeRegressor(criterion='friedman_mse')
# classifier.fit(x_train,y_train)
# print(classifier.score(x_test,y_test))#0.8903864111306338

'''Random Forests are effective when you have a complex dataset with many features and interactions, and you want to 
    reduce overfitting.'''
# classifier = RandomForestRegressor( n_estimators=100, criterion='friedman_mse')
# classifier.fit(x_train,y_train)
# print(classifier.score(x_test,y_test))#0.8817687851687781

# classifier = RandomForestRegressor(criterion='friedman_mse')
# classifier.fit(x_train,y_train)
# pickle.dump(classifier,open('demo','wb'))
# print(classifier.score(x_test,y_test))

# import pickle
# model = pickle.load(open('demo','rb'))
# print(model.score(x_test,y_test))#0.8850177209414091


''' KNeighborsRegressor is useful when local relationships between data points are important, and you expect the target 
    variable to have a smooth and continuous distribution.'''
# classifier = KNeighborsRegressor(n_neighbors=5)
# classifier.fit(x_train,y_train)
# print(classifier.score(x_test,y_test))#0.8707247919560175

# classifier = GaussianNB()
# classifier.fit(x_train,y_train)
# print(classifier.score(x_test,y_test))#

# classifier = MultinomialNB()
# classifier.fit(x_train,y_train)
# print(classifier.score(x_test,y_test))#

# classifier = BernoulliNB()
# classifier.fit(x_train,y_train)
# print(classifier.score(x_test,y_test))#


