#  Clean the dataset and update the CSV file

import pandas as pd

df = pd.read_csv("C:\\Users\\Owner\\Desktop\\PandasExercises\\Automobile_data.csv", na_values={
'price':["?", "n.a"],
'stroke':["?", "n.a"],
'horsepower':["?", "n.a"],
'peak-rpm':["?", "n.a"],
'average-mileage':["?", "n.a"]})
print(df)