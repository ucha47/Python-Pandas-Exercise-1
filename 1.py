#  From the given dataset print the first and last five rows

import pandas as pd

df = pd.read_csv("C:\\Users\\Owner\\Desktop\\PandasExercises\\Automobile_data.csv")
print(df.head(5))
print(df.tail(5))



