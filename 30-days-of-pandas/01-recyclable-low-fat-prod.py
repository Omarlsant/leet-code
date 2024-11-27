# 1757. Recyclable and low fat products
import pandas as pd

def recyclable_and_low_fat(products: pd.DataFrame) -> pd.DataFrame:
    # Filter products that are both low fat and recyclable
    filtered_products = products[(products['low_fats'] == 'Y') & (products['recyclable'] == 'Y')]
    
    # Select the required column
    result = filtered_products[['product_id']]
    
    return result
