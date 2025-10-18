# First prediction model using linear regression.
import pandas as pd
import numpy as np

Dataframe = pd.read_csv('Datasets/pizza_data.csv')
print(Dataframe.sample(20))

print(Dataframe.info())

print(Dataframe['Company'].nunique())

Dataframe['Price']  = Dataframe['Price'].str.replace('$', "", regex=False).astype(float)
print(Dataframe)

print(Dataframe.info())

df_encoded = pd.get_dummies(
    Dataframe,
    columns=['Company', 'Size', 'Type'],
    drop_first=True
)

print(df_encoded.head())

print(Dataframe['Type'].nunique())

print(df_encoded.columns)

# Number = Dataframe['Size'].nunique()
# print(Number)

# Unique_Sizes = Dataframe['Size'].unique()
# print(Unique_Sizes)