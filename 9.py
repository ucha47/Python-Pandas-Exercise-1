#  Concatenate two data frames using the following conditions
#  Create two data frames using the following two dictionaries.
import pandas as pd

GermanCars = {'Company': ['Ford', 'Mercedes', 'BMW', 'Audi'], 'Price': [23845, 171995, 135925, 71400]}
JapaneseCars = {'Company': ['Toyota', 'Honda', 'Nissan', 'Mitsubishi'], 'Price': [29995, 23600, 61500, 58900]}

carsDf1 = pd.DataFrame.from_dict(GermanCars)
carsDf2 = pd.DataFrame.from_dict(JapaneseCars)

uniteDf = pd.concat([carsDf1, carsDf2], keys=["German Cars", "Japanese Cars"])

print(uniteDf)
