# 2885. Rename Columns in a Pandas DataFrame
import pandas as pd  # Importing: pandas library for data manipulation

def renameColumns(students: pd.DataFrame) -> pd.DataFrame:
    # The renameColumns function receives a pandas DataFrame called 'students'
    # Rename the columns according to the specified mapping
    students = students.rename(columns={
        'id': 'student_id',
        'first': 'first_name',
        'last': 'last_name',
        'age': 'age_in_years'
    })
    # Return the DataFrame with the renamed columns
    return students

# Example usage
data = {
    'id': [1, 2, 3, 4, 5],
    'first': ['Mason', 'Ava', 'Taylor', 'Georgia', 'Thomas'],
    'last': ['King', 'Wright', 'Hall', 'Thompson', 'Moore'],
    'age': [6, 7, 16, 18, 10]
}

# Create a DataFrame from the dictionary of student data
students = pd.DataFrame(data)
# Call the function to rename the columns
result = renameColumns(students)
# Print the DataFrame with renamed columns
print(result)
