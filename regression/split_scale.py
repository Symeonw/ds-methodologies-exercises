import pandas as pd
import warnings
warnings.filterwarnings("ignore")
import numpy as numpy
import wrangle
import env


df = wrangle_telco()
train, test = train_test_split(df, train_size = .7, random_state = 123)
print(test)

def split_my_data(df,t_size,seed,split_on):
    from sklearn.model_selection import train_test_split
    x = df.drop([split_on], axis=1)
    y = df[split_on]
    x_train, x_test, y_train, y_test = train_test_split(x, y, train_size = t_size, random_state = seed)
    return x_train, x_test, y_train, y_test


split_my_data(df,.7,123,"tenure")


def standard_scaler():
    train = x_train,y_train
    from sklearn.preprocessing import StandardScaler, QuantileTransformer, PowerTransformer, RobustScaler, MinMaxScaler
    scaler = StandardScaler()
    output = scaler.fit(train):scaler.transform(train),scaler.transform(test)

standard_scaler()