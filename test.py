# This file is to test the performance of the saved model


# Start timer
import time
current_milli_time = lambda: int(round(time.time() * 1000))
startTime = current_milli_time()



# Load the dataset
import pandas
import numpy as np

dataset = pandas.read_csv('dataset/dataset.csv')



# Split Data
from sklearn.model_selection import train_test_split
array = dataset.values
X = array[:,0:15]
Y = array[:,15]
val_size = 0.2
seed=7
X_train, X_val, Y_train, Y_val = train_test_split(X,Y, test_size=val_size, random_state=seed)



import joblib
model = joblib.load('final_models/decision_tree.pkl')
# Model Evaluation
from sklearn import metrics
predictions = model.predict(X_val)
print(metrics.accuracy_score(Y_val, predictions))
print(metrics.confusion_matrix(Y_val, predictions))
print(metrics.classification_report(Y_val, predictions))