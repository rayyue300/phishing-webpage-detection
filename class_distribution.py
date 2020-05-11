import pandas
import numpy as np

dataset = pandas.read_csv('dataset/dataset.csv')

# Display the class distribution by histogram
import matplotlib.pyplot as plt
dataset.hist()
plt.show()