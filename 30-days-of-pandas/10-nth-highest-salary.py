# 177. Nth Highest Salary
import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    # Sort the salaries in ascending order
    employee.sort_values(by='salary', ascending=True, inplace=True)
    
    # Rank the salaries in descending order, ensuring unique ranks for duplicate values
    employee['rank'] = employee['salary'].rank(method='dense', ascending=False)
    
    # Remove duplicates based on the rank
    df = employee.drop_duplicates(subset='rank', keep='first')
    
    # Select the row with the nth highest rank
    df1 = df[df['rank'] == N]
    
    # Return the nth highest salary, or None if it does not exist
    return pd.DataFrame({'getNthHighestSalary({})'.format(N): [None if len(df1) == 0 else df1['salary'].iloc[0]]})
