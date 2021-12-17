#  Count total cars per company
#  კლებადობის მიხედვითაც დავალაგე

import pandas as pd

df = pd.read_csv("C:\\Users\\Owner\\Desktop\\PandasExercises\\Automobile_data.csv")
df = df.groupby(["company"]).size().reset_index(name='Number of cars').sort_values('Number of cars', ascending=False)

print(df)

#  df['company'].value_counts() UKETESIA