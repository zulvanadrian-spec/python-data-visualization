import pandas as pd

data = {
    "Product":["Laptop","Hand Phone","Mac Book"],
    "Price":[26000000,11000000,21000000]
}

df = pd.DataFrame(data)
print(df)