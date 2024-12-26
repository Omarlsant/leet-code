# 570. Manager with at Least 5 Direct Reports
import pandas as pd

def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    # Count the number of direct reports for each manager using value_counts on managerId column
    manager_counts = employee['managerId'].value_counts()
    # Filter managers with at least 5 direct reports and get their IDs
    qualified_managers = manager_counts[manager_counts >= 5].index
    # Get the names of qualified managers by filtering the original dataframe where id matches qualified manager IDs
    result = employee[employee['id'].isin(qualified_managers)][['name']]
    
    return result