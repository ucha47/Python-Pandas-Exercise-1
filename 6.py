#  Find each company’s Highest price car

import pandas as pd

df = pd.read_csv("C:\\Users\\Owner\\Desktop\\PandasExercises\\Automobile_data.csv")
car_Manufacturers = df.groupby('company')
priceDf = car_Manufacturers['company', 'price'].max()
print(priceDf)
