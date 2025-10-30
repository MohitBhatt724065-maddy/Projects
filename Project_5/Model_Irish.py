# Practicing on irish dataset.

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

Dataframe = pd.read_csv('/home/mohit-bhatt/Desktop/Projects/Projects/Projects/Datasets/iris.csv')

print(Dataframe)
print('-'*10)
Dataframe_Processed1 = Dataframe.drop('Unnamed: 0', axis=1)
print(Dataframe_Processed1)
print('-' * 10)


X = Dataframe_Processed1.drop('Species', axis=1)
y = Dataframe_Processed1['Species']


from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

from sklearn.neighbors import KNeighborsClassifier


knn_model = KNeighborsClassifier(n_neighbors=3)
knn_model.fit(X_train, y_train)

from sklearn.metrics import accuracy_score

y_pred = knn_model.predict(X_test)
print(accuracy_score(y_test, y_pred))

# Remaining to be done(Not encodede Species column)