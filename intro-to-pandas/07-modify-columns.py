# 2884. Modify Columns in a Table
import pandas as pd  # Importing: pandas library for data manipulation

def modifySalaryColumn(employees: pd.DataFrame) -> pd.DataFrame:
    # The modifySalaryColumn function receives a pandas DataFrame called 'employees'
    # Modify the 'salary' column by multiplying each value by 2
    employees['salary'] = employees['salary'] * 2
    # Return the updated DataFrame with modified salaries
    return employees

# Defining a dictionary with employee data
data = {
    'name': ['Jack', 'Piper', 'Mia', 'Ulysses'],
    'salary': [19666, 74754, 62509, 54866]
}

# Create a DataFrame from the dictionary of employee data
employees = pd.DataFrame(data)
# Call the function to modify the salary column
result = modifySalaryColumn(employees)
# Print the updated DataFrame with modified salaries
print(result)
