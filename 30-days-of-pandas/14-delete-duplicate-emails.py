# 196. Delete Duplicate Emails
import pandas as pd

def delete_duplicate_emails(person: pd.DataFrame) -> None:
    # Sort the person DataFrame by email and id to prioritize smallest id for duplicates
    person.sort_values(by=['email', 'id'], inplace=True)
    # Drop duplicates, keeping only the first (smallest id) entry for each email
    person.drop_duplicates(subset='email', keep='first', inplace=True)
    
