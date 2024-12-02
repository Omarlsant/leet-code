# 1517. Find users with valid emails
import pandas as pd

def valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    # Define a regex pattern for valid emails
    pattern = r'^[a-zA-Z][\w.-]*@leetcode\.com$'
    
    # Use pandas `str.match` to filter valid emails
    valid_users = users[users['mail'].str.match(pattern, na=False)]
    
    return valid_users
