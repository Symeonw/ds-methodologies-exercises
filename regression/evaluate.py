import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pydataset import data
from statsmodels.formula.api import ols
df = data("tips")
df.info()
total_bill = tips["total_bill"]
tips = tips["tips"]
regr = old('tip ~ total_bill', data=tips).fit()
tips["yhat"] = regr.predict(tips["total_bill"])
def plot_residuals(x,y,df):
    sns.residplot(x,y,data=df)
    plt.show()

def regression_errors(y, y_hat):
    sse = ((y-y_hat)**2).sum()
    ess = ((yhat-y.mean())**2).sum()
    tss = sse + ess
    mse = 

def baseline_mean_errors(y, y_hat):
    
def better_than_baseline(sse, sse_baseline):

def model_significance(old_model):
    return ols_model.rsquared, ols_model.f_pvalue
    

