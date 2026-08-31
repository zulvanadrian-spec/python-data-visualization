# Read a CSV File

import pandas as pd

df = pd.read_csv("../Fashion.csv", skiprows=1)

print(df)