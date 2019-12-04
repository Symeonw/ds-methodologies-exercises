import pandas as pd
import seaborn as sns
from sklearn import metrics
from scipy.stats import entropy
def get_df():
    df = pd.read_csv('docs.txt')
    df.rename(columns={"2018-01-26 09:55:03 / 1 8 97.105.19.61":"col"}, inplace=True)
    df["date"] = df.col.str[0:10]
    df["hour"] = df.col.str[11:19]
    df["direct"] = df.col.str[20:]
    df.drop(columns=["col"],inplace=True)
    df.date = pd.to_datetime(df.date)
    df.direct = df.direct.str.split(" ")
    df["direction"] = df.direct.str[0]
    df["num_1"] = df.direct.str[1]
    df["num_2"] = df.direct.str[2]
    df["ip_address"] = df.direct.str[3]
    df.drop(columns=["direct"],inplace=True)
    df.dropna(inplace=True)
    df.num_2 = df.num_2.str.strip()
    df.direction = df.direction.str.strip()
    df.num_2 = pd.to_numeric(df.num_2, errors='coerce')
    df.num_1 = df.num_1.astype(int)
    df.dropna(inplace=True)
    return df

df = get_df()



