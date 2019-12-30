from sklearn.tree import DecisionTreeClassifier
From sklearn.metrics import accuracy_score
Import pandas as pd
Import numpy as np

#  Read the data
Data = np.asarray(pd.read_csv('data.csv', header=None))
X = data[:,0:2]
Y = data[:,2]

print(Data)