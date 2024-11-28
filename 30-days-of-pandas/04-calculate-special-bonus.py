# 1873. Calculate Special Bonus
import pandas as pd

# Define a function to calculate a special bonus for employees based on specific criteria
def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    # Add a new column 'bonus' to the DataFrame based on a conditional calculation
    employees['bonus'] = employees.apply(
        # Assign 'salary' as 'bonus' if employee_id is odd and name does not start with 'M', otherwise assign 0
        lambda row: row['salary'] if row['employee_id'] % 2 != 0 and not row['name'].startswith('M') else 0, 
        axis=1  # Specify that the function operates on rows
    )
    # Return a DataFrame with only 'employee_id' and 'bonus', sorted by 'employee_id'
    return employees[['employee_id', 'bonus']].sort_values(by='employee_id')
