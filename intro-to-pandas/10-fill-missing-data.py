# 2887. Fill Missing Data in a DataFrame
import pandas as pd # Importing the pandas library for data manipulation.

def fillMissingValues(products: pd.DataFrame) -> pd.DataFrame:
    # Fill missing values in 'quantity' column with 0.
    products['quantity'].fillna(0, inplace=True)
    return products

# Assign the DataFrame to a variable and create a dictionary.
products = pd.DataFrame({
    'name': ['Wristwatch', 'WirelessEarbuds', 'GolfClubs', 'Printer'],
    'quantity': [None, None, 779, 849],
    'price': [135, 821, 9319, 3051]
})

# Apply the function to the DataFrame
filled_products = fillMissingValues(products)
print(filled_products)
