# 1741. Find Total Time Spent by Each Employee
import pandas as pd

def total_time(employees: pd.DataFrame) -> pd.DataFrame:
    # Calculate the total time for each entry
    employees['time_spent'] = employees['out_time'] - employees['in_time']
    # Group by emp_id and event_day, then sum the total time
    result = employees.groupby(['emp_id', 'event_day'], as_index=False)['time_spent'].sum()
    # Rename the columns to match the output format
    result.rename(columns={'event_day': 'day', 'time_spent': 'total_time'}, inplace=True)
    
    return result
