# 607. Sales Person
import pandas as pd

def sales_person(sales_person: pd.DataFrame, company: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    # Get all salespeople that have orders with RED company
    red_sales = orders[orders['com_id'].isin(
        company[company['name'] == 'RED']['com_id']
    )]['sales_id'].unique()
    # Filter salespeople who don't have RED orders
    result = sales_person[~sales_person['sales_id'].isin(red_sales)][['name']]
    
    return result