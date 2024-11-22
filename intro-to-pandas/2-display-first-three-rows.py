# 2879. Display the first three rows of the DataFrame
import pandas as pd  # Importing: pandas library for data manipulation
from typing import List  # Importing: List from typing for type annotation

def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    # The selectFirstRows function receives a pandas DataFrame called 'employees'
    # Get the first three rows of the DataFrame
    first_three_rows = employees.head(3)
    # Return the first three rows of the DataFrame
    return first_three_rows

# Define a dictionary with employee data
data = {
    'employee_id': [3, 90, 9, 60, 49, 43],
    'name': ['Bob', 'Alice', 'Tatiana', 'Annabelle', 'Jonathan', 'Khaled'],
    'department': ['Operations', 'Sales', 'Engineering', 'InformationTechnology', 'HumanResources', 'Administration'],
    'salary': [48675, 11096, 33805, 37678, 23793, 40454]
}

# Create a DataFrame from the dictionary of employee data
employees = pd.DataFrame(data)
# Call the function to select the first three rows of the DataFrame
result = selectFirstRows(employees)
# Print the first three rows of the DataFrame
print(result)
