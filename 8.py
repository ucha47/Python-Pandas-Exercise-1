#  Sort all cars by Price column

import pandas as pd

carsDf = pd.read_csv("C:\\Users\\Owner\\Desktop\\PandasExercises\\Automobile_data.csv")
carsDf = carsDf.sort_values(by=['price', 'horsepower'], ascending=False)
print(carsDf.head(5))

