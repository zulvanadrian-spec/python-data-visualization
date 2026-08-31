# Create a DataFrame with 3 columns

import pandas as pd

data = {
    "Product":["Road Bike","Running Shoes","Swimming Suit"],
    "Price":[25000000,5000000,2000000],
    "Stok":[2, 10, 8]
}

df = pd.DataFrame(data)
print(df)