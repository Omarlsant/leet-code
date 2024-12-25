# 1378. Replace Employee ID With The Unique Identifier
import pandas as pd

def replace_employee_id(employees: pd.DataFrame, employee_uni: pd.DataFrame) -> pd.DataFrame:
    # Merge the two dataframes on the 'id' column
    merged_df = pd.merge(employees, employee_uni, on='id', how='left')
    # Select and rearrange the columns to match the required format
    result = merged_df[['unique_id', 'name']]
    
    return result
