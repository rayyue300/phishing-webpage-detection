# Start timer
import time
startTime = time.time()



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
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import StratifiedKFold
model = DecisionTreeClassifier()
model.fit(X_train,Y_train)



# Plot the tree
from sklearn.tree import plot_tree
import matplotlib.pyplot as plt
plt.figure(figsize=(16,9))
plot_tree(model, 
    feature_names=dataset.columns,
    filled=True, 
    rounded=True, 
    fontsize=6,
    impurity=False,)
plt.savefig('tree_high_dpi', dpi=100)



# Model Evaluation
from sklearn import metrics
predictions = model.predict(X_val)
print(metrics.accuracy_score(Y_val, predictions))
print(metrics.confusion_matrix(Y_val, predictions))
print(metrics.classification_report(Y_val, predictions))



# Save the model
import joblib
joblib.dump(model, 'final_models/decision_tree.pkl')



# Print Elapsed Time
print('Elapsed time: '+str(round(time.time()-startTime))+'s')