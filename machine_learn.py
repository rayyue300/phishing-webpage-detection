#https://archive.ics.uci.edu/ml/datasets/Phishing+Websites
import pandas
import numpy as np
dataset = pandas.read_csv('dataset/dataset.csv')

from sklearn.model_selection import train_test_split
array = dataset.values
X = array[:,0:10]
Y = array[:,10]
val_size = 0.2
seed=7
X_train, X_val, Y_train, Y_val = train_test_split(X,Y, test_size=val_size, random_state=seed)


# logistic regression approach
from sklearn import metrics
from sklearn.linear_model import LogisticRegression
LR = LogisticRegression(solver='lbfgs')
LR.fit(X_train,Y_train)
predictions = LR.predict(X_val)
print(metrics.accuracy_score(Y_val, predictions))
print(metrics.confusion_matrix(Y_val, predictions))
print(metrics.classification_report(Y_val, predictions))

# decision tree
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier
DT = DecisionTreeClassifier()
DTTrainModel = DT.fit(X_train, Y_train)
predictions = DT.predict(X_val)
print(metrics.accuracy_score(Y_val, predictions))
print(metrics.confusion_matrix(Y_val, predictions))
print(metrics.classification_report(Y_val, predictions))

# random forest

from sklearn.ensemble import RandomForestClassifier

# Create the model with 10 trees
model = RandomForestClassifier(n_estimators=10, 
                               bootstrap = True,
                               max_features = 'sqrt')
# Fit on training data
model.fit(X_train, Y_train)

RFpredictions = model.predict(X_val)
print(metrics.accuracy_score(Y_val, RFpredictions))
print(metrics.confusion_matrix(Y_val, RFpredictions))
print(metrics.classification_report(Y_val, RFpredictions))

