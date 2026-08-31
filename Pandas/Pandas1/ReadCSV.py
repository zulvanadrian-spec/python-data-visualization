import pandas as pd

import pandas as pd

df = pd.read_csv("Fashion.csv", skiprows=1)

df.columns = [
    "Order ID", "Order Date", "Customer Name", "City", "Product Name",
    "Unit Price", "Quantity", "Discount (%)", "Subtotal", "Discount Amount",
    "Total Sales", "Shipping Fee", "Grand Total", "Payment Method",
    "Order Status", "Platform", "Customer Rating", "Size", "Material", "Gender"
]

print(df)
print("\n5 Data pertama : \n",df.head()) # display first five rows
print("\n5 Data terakhir : \n",df.tail()) # display the last five rows
print("\nUkuran Dataset : \n",df.shape) # check a size of dataset
print("\nNama-nama Kolom : \n",df.columns) # display columns name