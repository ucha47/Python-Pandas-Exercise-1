#  Create two data frames using the following two Dicts, Merge two data frames,
#  and append the second data frame as a new column to the first data frame.
import pandas as pd

Car_Price = {'Company': ['Toyota', 'Honda', 'BMW', 'Audi'], 'Price': [23845, 17995, 135925, 71400]}
Car_Horsepower = {'Company': ['Toyota', 'Honda', 'BMW', 'Audi'], 'horsepower': [141, 80, 182, 160]}

priceDf = pd.DataFrame.from_dict(Car_Price)
horsepowerDf = pd.DataFrame.from_dict(Car_Horsepower)

mergedDf = pd.concat([priceDf, horsepowerDf], axis=1)

print(mergedDf)
