import acquire
import pandas as pd 
import numpy as np
import warnings
warnings.filterwarnings("ignore")
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import MinMaxScaler
import pandas_profiling
df = get_titanic_data()
profile = pandas_profiling.ProfileReport(df)
profile.get_rejected_variables(threshold=.9)
df.isnull().sum()
df.age.value_counts(bins=9, sort=True)
df.embarked.value_counts(dropna=False)
df.age.value_counts(dropna=False)
df.drop(columns=["deck"], inplace=True)
df.fillna(np.nan, inplace=True)
train, test = train_test_split(df, train_size=.8, random_state=123)
train.age.value_counts(dropna=False)
imp_mode = SimpleImputer(missing_values=np.nan, strategy="most_frequent")
imp_mode.fit(train[["embarked"]])
train["embarked"]=imp_mode.transform(train[["embarked"]])
test["embarked"]=imp_mode.transform(test[["embarked"]])
train.embarked.value_counts()
imp_median = SimpleImputer(missing_values=np.nan, strategy="median")
train['age'] = imp_median.fit_transform(train[['age']])
train.age.isnull().sum()
int_encoder = LabelEncoder()
int_encoder.fit(train.embarked)
train.embarked = int_encoder.transform(train.embarked)
train.embarked.value_counts()
embarked_array = np.array(train.embarked)
embarked_array[0:5]
embarked_array = embarked_array.reshape(len(embarked_array),1)
ohe = OneHotEncoder(sparse=False, categories="auto")
embarked_ohe = ohe.fit_transform(embarked_array)
embarked_test_ohe = ohe.transform(embarked_array)
embarked_test_ohe[0:5]