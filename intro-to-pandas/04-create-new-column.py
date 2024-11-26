# 2881. Create a new column in a DataFrame
import pandas as pd  # Importing: pandas library for data manipulation

def createBonusColumn(employees: pd.DataFrame) -> pd.DataFrame:
    # The createBonusColumn function receives a pandas DataFrame called 'employees'
    # Create a new column 'bonus' which is twice the 'salary' column
    employees['bonus'] = employees['salary'] * 2
    # Return the updated DataFrame with the new 'bonus' column
    return employees

# Define a dictionary with employee data
data = {
    'name': ['Piper', 'Grace', 'Georgia', 'Willow', 'Finn', 'Thomas'],
    'salary': [4548, 28150, 1103, 6593, 74576, 24433]
}

# Create a DataFrame from the dictionary of employee data
employees = pd.DataFrame(data)
# Call the function to create the bonus column in the DataFrame
result = createBonusColumn(employees)
# Print the updated DataFrame with the new 'bonus' column
print(result)
