# import libraries
import numpy as np
import pandas as pd
from sklearn.neighbors import KNeighborsRegressor

"""### Load Dataset"""

# load dataset
from sklearn.datasets import load_breast_cancer

data = load_breast_cancer()
# create dtaframe
pd.set_option('display.max_column',None)
pd.set_option('display.width',False)

df = pd.DataFrame(np.c_[data.data, data.target], columns=[list(data.feature_names) + ['target']])


"""### Split Data"""

X = df.iloc[:, 0:-1]
y = df.iloc[:, -1]

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=2020)

# print('Shape of X_train = ', X_train.shape)
# print('Shape of y_train = ', y_train.shape)
# print('Shape of X_test = ', X_test.shape)
# print('Shape of y_test = ', y_test.shape)

"""## Train Naive Bayes Classifier Model"""

classifier = KNeighborsRegressor(n_neighbors=5)
classifier.fit(X_train,y_train)
print(classifier.score(X_test,y_test))
# print(classifier.score(X_test, y_test))

# patient1 = np.array([patient1])
# patient1
#
# classifier.predict(patient1)
#
# data.target_names
#
# pred = classifier.predict(patient1)
#
# if pred[0] == 0:
#     print('Patient has Cancer (malignant tumor)')
# else:
#     print('Patient has no Cancer (malignant benign)')





'''# import libraries
import numpy as np
import pandas as pd
 
"""### Load Dataset"""
 
#load dataset
from sklearn.datasets import load_breast_cancer
data = load_breast_cancer()
 
data.data
 
data.feature_names
 
data.target
 
data.target_names
 
# create dtaframe
df = pd.DataFrame(np.c_[data.data, data.target], columns=[list(data.feature_names)+['target']])
df.head()
 
df.tail()
 
df.shape
 
"""### Split Data"""
 
X = df.iloc[:, 0:-1]
y = df.iloc[:, -1]
 
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=2020)
 
print('Shape of X_train = ', X_train.shape)
print('Shape of y_train = ', y_train.shape)
print('Shape of X_test = ', X_test.shape)
print('Shape of y_test = ', y_test.shape)
 
"""## Train Naive Bayes Classifier Model"""
 
from sklearn.naive_bayes import GaussianNB
 # Suitable for continuous features with a normal distribution.

classifier = GaussianNB()
classifier.fit(X_train, y_train)
 
classifier.score(X_test, y_test)
 
# features follow a multinomial distribution, which is suitable for discrete data
from sklearn.naive_bayes import MultinomialNB
classifier_m = MultinomialNB()
classifier_m.fit(X_train, y_train)
 
classifier_m.score(X_test, y_test)
 
 # features are binary (0 or 1), representing the presence or absence of a particular feature.
from sklearn.naive_bayes import BernoulliNB
classifier_b = BernoulliNB()
classifier_b.fit(X_train, y_train)
 
classifier_b.score(X_test, y_test)
 
"""## Predict Cancer"""
 
patient1 = [17.99,
 10.38,
 122.8,
 1001.0,
 0.1184,
 0.2776,
 0.3001,
 0.1471,
 0.2419,
 0.07871,
 1.095,
 0.9053,
 8.589,
 153.4,
 0.006399,
 0.04904,
 0.05373,
 0.01587,
 0.03003,
 0.006193,
 25.38,
 17.33,
 184.6,
 2019.0,
 0.1622,
 0.6656,
 0.7119,
 0.2654,
 0.4601,
 0.1189]
 
patient1 = np.array([patient1])
patient1
 
classifier.predict(patient1)
 
data.target_names
 
pred = classifier.predict(patient1)
 
if pred[0] == 0:
  print('Patient has Cancer (malignant tumor)')
else:
  print('Patient has no Cancer (malignant benign)')'''