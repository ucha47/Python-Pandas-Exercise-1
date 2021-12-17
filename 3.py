#  Print most expensive car’s company name and price.

import pandas as pd

df = pd.read_csv("C:\\Users\\Owner\\Desktop\\PandasExercises\\Automobile_data.csv")
df = df[['company', 'price']][df.price == df['price'].max()]
print(df)