import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

test = pd.read_csv(r"C:\Users\Joshi Ajay\Downloads\test.csv")
train = pd.read_csv("C:\\Users\\Joshi Ajay\\Downloads\\train.csv")

x_train = train.drop(columns='SalePrice')
y_train = train['SalePrice']
x_test = test.copy()

num_val = x_train.select_dtypes(include=['int64','float64'])
cat_val = x_train.select_dtypes(include=['O'])

'''columns with null values'''
cat_val_miss = [ var for var in cat_val.columns if cat_val[var].isnull().sum()>0]
num_val_miss = [ var for var in num_val.columns if num_val[var].isnull().sum()>0]

'''column without null values'''
cat_val_not_miss = [ var for var in cat_val.columns if var not in cat_val_miss]
num_val_not_miss = [ var for var in num_val.columns if var not in num_val_miss]

# print(cat_val_miss)
# print(num_val_miss)

num_mean = ['LotFrontage']
num_median = ['MasVnrArea', 'GarageYrBlt']
cat_mode = ['Alley', 'MasVnrType', 'BsmtQual', 'BsmtCond', 'BsmtExposure', 'BsmtFinType1', 'BsmtFinType2',
            'Electrical', 'FireplaceQu']
cat_const = ['GarageType', 'GarageFinish', 'GarageQual', 'GarageCond', 'PoolQC', 'Fence', 'MiscFeature']

num_mean_imputer = Pipeline(steps=[('impute',SimpleImputer(strategy='mean'))])
num_median_imputer = Pipeline(steps=[('impute',SimpleImputer(strategy='median'))])
cat_mode_imputer = Pipeline(steps=[('impute',SimpleImputer(strategy='most_frequent'))])
cat_const_imputer = Pipeline(steps=[('impute',SimpleImputer(strategy='constant', fill_value='missing'))])
'''
    --> Pipeline is used to sequentially apply a list of transforms and a final estimator. 
    --> ColumnTransformer is a class in scikit-learn that allows you to selectively apply 
        different transformers to different columns in your dataset.    
'''

preprocessor = ColumnTransformer(transformers=[
    ("mean_imputer", num_mean_imputer, num_mean),
    ("median_imputer", num_median_imputer, num_median),
    ("mode_imputer", cat_mode_imputer, cat_mode),
    ("missing_imputer", cat_const_imputer, cat_const)
    ],
    )

preprocessor.fit(x_train)

'''
    The fit method is used to compute necessary information based on the input data (x_train).
'''

x_train_clean = preprocessor.transform(x_train)
x_test_clean = preprocessor.transform(x_test)
'''
    preprocessor.transform(x_train):
    The transform method applies the transformations learned during the fit step to the input data (x_train).
'''

new_train = pd.DataFrame(x_train_clean,columns=num_mean+num_median+cat_mode+cat_const)
'''
    transform will return numpy array so will create an datafame form array with column name mantioned
'''
X_train =  pd.concat([new_train, train[cat_val_not_miss], train[num_val_not_miss]], axis=1)
'''
    here in all processe column with not null values be be removed so we will concatinate those column
'''
# print(X_train.isnull().sum().sum())