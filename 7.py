#  Find the average mileage of each car making company

import pandas as pd

df = pd.read_csv("C:\\Users\\Owner\\Desktop\\PandasExercises\\Automobile_data.csv")
cmpn = df.groupby('company')
averageDf = cmpn['company', 'average-mileage'].mean()
print(averageDf)
