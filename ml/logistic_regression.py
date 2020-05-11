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
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import StratifiedKFold
import matplotlib.pyplot as plt

modelsLogRegs = []
modelsLogRegs.append(('lbfgs', LogisticRegression(solver='lbfgs', multi_class='ovr')))
modelsLogRegs.append(('liblinear', LogisticRegression(solver='liblinear', multi_class='ovr')))
modelsLogRegs.append(('sag', LogisticRegression(solver='sag', multi_class='ovr')))
modelsLogRegs.append(('saga', LogisticRegression(solver='saga', multi_class='ovr')))

resultsLogRegs = []
namesLogRegs=[]
print('ALG\tMEAN\tSTD')
for name, model in modelsLogRegs:
    kfold = StratifiedKFold(n_splits=10, random_state=7)
    cv_results = cross_val_score(model, X_train, Y_train, cv=kfold, scoring='accuracy')
    resultsLogRegs.append(cv_results)
    namesLogRegs.append(name)
    print('%s:\t%f\t(%f)' % (name, cv_results.mean(), cv_results.std()))



# Compare Algorithms
plt.boxplot(resultsLogRegs, labels=namesLogRegs)
plt.title('Logistic Regression')
#plt.show()



# Print Training Time
print('Training time: '+str(round(current_milli_time()-startTime))+'ms')
startTime = current_milli_time()


# Predictions on validation dataset using the “best” LR model
from sklearn import metrics
optimalAlg = 'sag'
#optimalAlg = input('Input optimal algorithm: ')
logReg = LogisticRegression(solver=str(optimalAlg), multi_class='ovr')
logReg.fit(X_train,Y_train)
predictions = logReg.predict(X_val)
print(metrics.accuracy_score(Y_val, predictions))
print(metrics.confusion_matrix(Y_val, predictions))
print(metrics.classification_report(Y_val, predictions))



# Save the model
import joblib
joblib.dump(logReg, 'final_models/logistic_regression.pkl')



# Print Testing Time
print('Testing time: '+str(round(current_milli_time()-startTime))+'ms')