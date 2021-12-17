#  Print All Toyota Cars details

import pandas as pd

df = pd.read_csv("C:\\Users\\Owner\\Desktop\\PandasExercises\\Automobile_data.csv")
car_Manufacturers = df.groupby('company')
toyotaDf = car_Manufacturers.get_group('toyota')
print(toyotaDf)
