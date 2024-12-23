# 586. Customer Placing the Largest Number of Orders
import pandas as pd

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    # Group by customer_number and count the orders
    order_counts = orders.groupby('customer_number').size().reset_index(name='order_count')
    # Find the maximum number of orders
    max_orders = order_counts['order_count'].max()
    # Filter to get the customer_number(s) with the maximum number of orders
    result = order_counts[order_counts['order_count'] == max_orders][['customer_number']]
    
    return result
