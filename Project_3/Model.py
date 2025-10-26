# Model practice on Social_Media_Network_Ads
import pandas as pd

Dataframe = pd.read_csv('/home/mohit-bhatt/Desktop/Projects/Projects/Datasets/Social_Network_Ads.csv')

print(Dataframe.sample(10))

X = Dataframe.iloc[:, 1:4]
# print(X.sample(10))

y = Dataframe.iloc[:, 4]
# print(y.sample(10))

X = pd.get_dummies(X, columns=['Gender'],  drop_first=True)

print(X.sample(10))