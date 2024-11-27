# 183. Customers Who Never Order
import pandas as pd  # Import pandas library for data manipulation.

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    # Select customers whose IDs are not in the orders' customerId column.
    no_orders = customers[~customers['id'].isin(orders['customerId'])]  

    # Return a DataFrame with the 'name' column renamed to 'Customers'.
    return no_orders[['name']].rename(columns={'name': 'Customers'})  
