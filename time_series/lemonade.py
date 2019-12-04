import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv("lemonade.csv")
df.describe()



def outlier_detect(df, std_amount):
    df = df.drop(columns=["Date", "Day"])
    for col in df.columns:
        df[col].astype(float)
        sorted(df[col])
        Q1,Q3 = np.percentile(df[col], [25,75])
        IQR = Q3 - Q1
        lower_range = Q1 - (std_amount * IQR)
        upper_range = Q3 + (std_amount * IQR)
        print(f"Lower range for {col} is {lower_range}, upper range is {upper_range}")
 
outlier_detect(df,1.5)
#Temp: lower range is not convicing, upper range seems reasonable(depending on province)
#Rainfall: not enough domain knowlage to understand implications of varying amounts of rainfall
#Flyers: Lower range seems resonable, upper range seems a bit high. 
#Price: Both ranges are equal, and agreeable. 
#Sales Both ranges are agreeable
outlier_detect(df,3)
#Temp: Ranges are not agreeable
#Rainfall: not enough domain knowlage to understand implication of varying amounts of rainfall
#Flyers: Lower bound not possiable, upper bound potentially reasonable
#Price: is equal and resonable.
#Sales: Not possiable to have negitive sales. 

def plot_dist(df):
    df = df.drop(columns=["Date","Day"])
    for col in df.columns:
        df[col].astype(float)
        sns.distplot(df[col])
        plt.show()
plot_dist(df)