import acquire
import prepare 
import stats
from sklearn.tree import DecisionTreeClassifier
df = get_iris_data()
df.columns
df.dropna(inplace=True)
df.species_name.value_counts(dropna=False)
encoder = LabelEncoder()
encoder.fit(df.species_name)
df.species_name = encoder.transform(df.species_name)
logit.fit(X_train, y_train)
X = df[["sepal_length", "sepal_width", "petal_length", "petal_width"]]
y = df[["species_name"]]

X_train, X_test, y_train, y_test = train_test_split(X, y, train_size = .80, random_state = 123)
X_train.head()
y_train.head()
logit = LogisticRegression(C=1, class_weight={1:2}, random_state = 123, solver='liblinear')
logit.fit(X_train, y_train)
logit.coef_
logit.intercept_
y_pred = logit.predict(X_train)
y_pred_proba = logit.predict_proba(X_train)
logit.score(X_train, y_train)
confusion_matrix(y_train, y_pred)
print(classification_report(y_train, y_pred))
logit.score(X_test, y_test)
#newton-cg .8888888
#saga .8444444
#lbfgs .88888
# sag .88888
#liblinear .91111111

y_pred_proba = [i[1] for i in y_pred_proba]
fig = plt.figure()
ax = fig.add_subplot(111)
ax.scatter(y_pred_proba, y_pred)
#Liblinear preforms the best



clf = DecisionTreeClassifier(criterion='entropy', max_depth=4, random_state=123)
clf.fit(X_train, y_train)
y_pred = clf.predict(X_train)
y_pred[0:5]
clf.score(X_train, y_train)
confusion_matrix(y_train, y_pred)
labels = sorted(y_train.species_name.unique())
pd.DataFrame(confusion_matrix(y_train, y_pred), index=labels, columns=labels)
print(classification_report(y_train, y_pred))
clf.score(X_test, y_test)
plt.figure()
clf_matrix = confusion_matrix(y_train, y_pred)
from sklearn.datasets import load_iris
iris = load_iris()
clf = DecisionTreeClassifier()
clf = clf.fit(iris.data, iris.target)
import graphviz
from sklearn.tree import export_graphviz
from graphviz import Graph 
dot_data = export_graphviz(clf, out_file=None)
graph = graphviz.Source(dot_data)
graph.render('iris_decision_tree', view=True)

rf = RandomForestClassifier(bootstrap=True, class_weight=None, criterion="gini", min_samples_leaf=1, n_estimators=100, max_depth=3, random_state=123)
rf.fit(X_train, y_train)
print(rf.feature_importances_)
y_pred = rf.predict(X_train)
y_pred_proba = rf.predict_proba(X_train)
rf.score(X_train, y_train)
confusion_matrix(y_train, y_pred)
print(classification_report(y_train, y_pred))
rf.score(X_test, y_test)


df_2 = get_titanic_data()
df_2.dropna(inplace=True)
X_2 = df_2[['pclass','age','fare','sibsp','parch']]
y_2 = df_2.survived

X_train_2, X_test_2, y_train_2, y_test_2 = train_test_split(X_2, y_2, test_size = .25, random_state = 123)

rf_2 = RandomForestClassifier(bootstrap=True, class_weight=None, criterion='entropy', min_samples_leaf=1, n_estimators=10000, max_depth=5, random_state=123)

rf_2.fit(X_train_2, y_train_2)

print(rf_2.feature_importances_)
y_pred_2 = rf_2.predict(X_train_2)
y_pred_proba_2 = rf_2.predict_proba(X_train_2)
rf_2.score(X_train_2, y_train_2)
confusion_matrix(y_train_2, y_pred_2)
print(classification_report(y_train_2, y_pred_2))
rf_2.score(X_test_2, y_test_2)

