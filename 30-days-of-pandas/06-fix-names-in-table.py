# 1667. Fix Names in a Table
import pandas as pd

def fix_names(users: pd.DataFrame) -> pd.DataFrame:
    # Apply title case to the 'name' column to capitalize the first letter and lowercase the rest
    users['name'] = users['name'].str.capitalize()
    
    # Return the result sorted by 'user_id'
    result = users.sort_values(by='user_id')
    
    return result
