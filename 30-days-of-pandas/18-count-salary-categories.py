# 1907. Count Salary Categories
import pandas as pd

def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:
    # Define the salary categories with precise conditions
    low_salary = accounts['income'] < 20000
    average_salary = (accounts['income'] >= 20000) & (accounts['income'] <= 50000)
    high_salary = accounts['income'] > 50000
    
    # Count accounts in each category
    result = pd.DataFrame([
        {'category': 'Low Salary', 'accounts_count': low_salary.sum()},
        {'category': 'Average Salary', 'accounts_count': average_salary.sum()},
        {'category': 'High Salary', 'accounts_count': high_salary.sum()}
    ])
    
    return result
