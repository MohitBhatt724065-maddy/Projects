# Working on dataset viz.
Data  = {
    'Name': ['Milan', 'Samir', 'Miraz', 'Nitish', 'Andrej'],
    'Age': [21, 32, None, 23, 32],
    'Salary': ['USD 1000', None, 'USD 2000', 'USD 3000', 'USD 4000']
}
import pandas as pd
Dataframe = pd.DataFrame(Data)
print(Dataframe)

print(Dataframe.isnull().sum())


Dataframe['Salary'] = Dataframe['Salary'].str.replace('USD', '', regex=False).astype(float)
print(Dataframe)
# DF_processed = Dataframe.dropna()
# print('--'*10)
# print(DF_processed)

Dataframe_Median_Age = Dataframe['Age'].median()
Dataframe_Median_SAlary = Dataframe['Salary'].median()

Dataframe['Age'] = Dataframe['Age'].fillna(Dataframe_Median_Age)
Dataframe['Salary'] = Dataframe['Salary'].fillna(Dataframe_Median_SAlary)
print('--' * 10)

print(Dataframe)