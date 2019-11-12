import pandas as pd
from pydataset import data
import seaborn as sns
from sklearn.metrics import r2_score
df = data("faithful")

df.corr()

sns.kdeplot(df)
sns.pairplot(df)

from sklearn.model_selection import train_test_split
train, test = train_test_split(df, train_size = .8, random_state = 123)
X_train = train.drop(columns="eruptions")
y_train = train.eruptions
X_test = test.drop(columns = "eruptions")
y_test = test.eruptions

from sklearn.linear_model import LinearRegression
lm = LinearRegression()
lm.fit(X_train, y_train)
y_pred = lm.predict(X_train)


lm.score(X_test, y_test)
r2 = r2_score(y_train, y_pred)

sns.regplot(X_train, y_train, fit_reg=True)

import matplotlib.pyplot as plt

_, ax = plt.subplots()

ax.scatter(x = range(0, y_train.size), y=y_train, c = 'blue', label = 'Actual', alpha = .7)
ax.scatter(x = range(0, y_pred.size), y=y_pred, c = 'red', label = 'Predicted', alpha = 0.5)

plt.title('Actual and predicted values')
plt.xlabel('Observations')
plt.ylabel('Eruptions')
plt.legend()
plt.yticks(range(1,6))
plt.text(45,5.4, f"rmse: {r2:.4f}")
plt.show()
