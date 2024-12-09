# 1795. Rearrange Products Table
import pandas as pd

def rearrange_products_table(products: pd.DataFrame) -> pd.DataFrame:
    # Melt the DataFrame to convert wide format to long format
    melted = products.melt(id_vars=['product_id'], value_vars=['store1', 'store2', 'store3'], var_name='store', value_name='price')
    # Drop rows where price is null
    melted.dropna(subset=['price'], inplace=True)    
    # Return the final result with the columns product_id, store, and price
    result = melted[['product_id', 'store', 'price']]
    
    return result
