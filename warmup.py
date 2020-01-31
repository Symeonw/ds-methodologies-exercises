from pydataset import data
from sklearn.model_selection import train_test_split

data('voteincome', show_doc=True)

df = data('voteincome')

df.drop(columns=["state", "year"], inplace=True)
X = df.drop(columns=["vote"])
y = df.vote


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=123, stratify=y)


from sklearn.neighbors import KNeighborsClassifierfrom 
from sklearn.metrics import classification_report
    
for i in range(1,5):
    clf = KNeighborsClassifier(n_neighbors=i)
    clf.fit(X_train, y_train)
    print(clf.score(X_test, y_test))


for i in range(1,5):
    clf = KNeighborsClassifier(n_neighbors=i)
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)
    print(classification_report(y_test, y_pred))




from sklearn import __version__
__version__






