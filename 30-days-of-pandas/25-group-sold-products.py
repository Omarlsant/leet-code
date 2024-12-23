# 1484. Group Sold Products By The Date
import pandas as pd

def categorize_products(activities: pd.DataFrame) -> pd.DataFrame:
    # Remove duplicates to ensure counting distinct products
    activities = activities.drop_duplicates()
    # Group by sell_date and aggregate the products
    grouped = activities.groupby('sell_date').agg({
        'product': lambda x: ','.join(sorted(x))
    }).reset_index()
    # Add a column for the number of distinct products
    grouped['num_sold'] = grouped['product'].apply(lambda x: len(x.split(',')))
    # Rename the columns as required
    grouped.rename(columns={'product': 'products'}, inplace=True)
    # Reorder columns as required
    result = grouped[['sell_date', 'num_sold', 'products']]
    # Order by sell_date
    result = result.sort_values(by='sell_date').reset_index(drop=True)
    
    return result
