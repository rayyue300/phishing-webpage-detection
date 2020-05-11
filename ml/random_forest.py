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



# Model Building
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import StratifiedKFold
import matplotlib.pyplot as plt

modelsRF = []
for x in range(10, 101, 10):
    modelsRF.append((str(x), RandomForestClassifier(n_estimators=x)))


resultsRF = []
namesRF=[]
print('ALG\tMEAN\tSTD')
for name, model in modelsRF:
    kfold = StratifiedKFold(n_splits=10, random_state=7)
    cv_results = cross_val_score(model, X_train, Y_train, cv=kfold, scoring='accuracy')
    resultsRF.append(cv_results)
    namesRF.append(name)
    print('%s:\t%f\t(%f)' % (name, cv_results.mean(), cv_results.std()))



# Compare Algorithms
plt.boxplot(resultsRF, labels=namesRF)
plt.title('Random Forest')
#plt.show()



# Print Training Time
print('Training time: '+str(round(current_milli_time()-startTime))+'ms')
startTime = current_milli_time()



# Predictions on validation dataset using the “best” RF model
from sklearn import metrics
optimalNo = 60
#optimalNo = input('Input optimal number: ')
model = RandomForestClassifier(n_estimators=int(optimalNo))
model.fit(X_train,Y_train)
predictions = model.predict(X_val)
print(metrics.accuracy_score(Y_val, predictions))
print(metrics.confusion_matrix(Y_val, predictions))
print(metrics.classification_report(Y_val, predictions))



# Save the model
import joblib
joblib.dump(model, 'final_models/random_forest.pkl')



# Print Testing Time
print('Testing time: '+str(round(current_milli_time()-startTime))+'ms')