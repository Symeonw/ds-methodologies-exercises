import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import cm
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.preprocessing import LabelEncoder
from mpl_toolkits.mplot3d import Axes3D

df = pd.read_csv("reddit.csv")
df.describe()
from scipy import stats
import numpy as np
df.rename(columns={"24":"Female", "25":"Male", "3iwivb": "Unknown", "I'm [25/M] having issues with my GF [24/F] Facebook profile":"Post"}, inplace = True)
kmeans = KMeans(n_clusters=6)
X = df.drop(columns=["Unknown", "Post"])
X["Male"] = X[X["Male"] < 100]
X["Female"] = X[X["Female"] < 100]
X["age_diff"] = (X.Male - X.Female).abs()
kmeans.fit(X)
X["cluster"] = kmeans.predict(X)
kmeans.cluster_centers_
X.describe()

df_subset = X[["Female", "Male"]]

k_values = []
inertias = []

for k in range(1, 10):
    kmeans = KMeans(n_clusters=k).fit(df_subset)
    inertias.append(kmeans.inertia_)
    k_values.append(k)

plt.plot(k_values, inertias, marker='x')
plt.xlabel('K')
plt.ylabel('inertia')
sns.relplot(data=X, y='Male', x='Female', size = 1, hue='cluster', palette="hot_r")
plt.scatter(x=kmeans.cluster_centers_[:, 0], y=kmeans.cluster_centers_[:, 1], marker='x', s=2000)


sns.relplot(data=X, hue=kmeans.labels_, x='Male', y='Female')

from fcmeans import FCM
from sklearn.datasets import make_blobs
from matplotlib import pyplot as plt
from seaborn import scatterplot as scatter

# fit the fuzzy-c-means
fcm = FCM(n_clusters=6)
fcm.fit(X)

# outputs
fcm_centers = fcm.centers
fcm_labels  = fcm.u.argmax(axis=1)


f, axes = plt.subplots(1, 2, figsize=(11,5))
scatter(X["Female"], X["Male"], ax=axes[0])
scatter(X["Female"], X["Male"], ax=axes[1], hue=fcm_labels)
scatter(fcm_centers["Female"], fcm_centers["Male"], ax=axes[1],marker="s",s=200)
plt.show()