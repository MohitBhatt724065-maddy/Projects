# Model practice on Social_Media_Network_Ads
import pandas as pd

Dataframe = pd.read_csv('/home/mohit-bhatt/Desktop/Projects/Projects/Datasets/Social_Network_Ads.csv')

# print(Dataframe.sample(10))
print(Dataframe)
X = Dataframe.iloc[:, 1:4]
# print(X.sample(10))

y = Dataframe.iloc[:, 4]
# print(y.sample(10))

X = pd.get_dummies(X, columns=['Gender'],  drop_first=True)

print(X.sample(10))

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)