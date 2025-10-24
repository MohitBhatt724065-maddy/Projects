import pandas as pd

Dataframe = pd.read_csv('/home/mohit-bhatt/Desktop/Projects/Projects/Datasets/HousingData.csv')

# print(Dataframe.sample(50))

print(Dataframe.info())


print(Dataframe.isnull().sum())

cont_col = ['CRIM', 'ZN', 'INDUS','AGE',  'LSTAT']

# for col in cont_col:
#     Dataframe[col].fillna(Dataframe[col].median(), inplace=True)
    
# print(Dataframe.isnull().sum())

for col in cont_col:
    median_value = Dataframe[col].median()
    Dataframe[col] = Dataframe[col].fillna(median_value)
    
print(Dataframe.isnull().sum())


# Fillin the CHAS column with binary values or dummy variables

mode_value = Dataframe['CHAS'].mode()[0]

Dataframe['CHAS'] = Dataframe['CHAS'].fillna(mode_value)


print(Dataframe.isnull().sum())

import matplotlib.pyplot as plt

plt.figure(figsize=(15, 12))

columns_name = Dataframe.columns

for i, cols in enumerate(columns_name):
    plt.subplot(4, 4, i + 1)
    Dataframe[cols].hist(bins=30, edgecolor='black', color='#1f77b4')
    plt.title(cols, fontsize=12)
    
plt.show()