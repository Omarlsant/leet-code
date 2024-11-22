# 2883. Drop Missing Data
import pandas as pd  # Importing: pandas library for data manipulation

def dropMissingData(students: pd.DataFrame) -> pd.DataFrame:
    # The dropMissingData function receives a pandas DataFrame called 'students'
    # Drop rows where the 'name' column has missing data (NaN)
    cleaned_students = students.dropna(subset=['name'])
    # Return the DataFrame with missing names removed
    return cleaned_students

# Define a dictionary with student data
data = {
    'student_id': [32, 217, 779, 849],
    'name': ['Piper', None, 'Georgia', 'Willow'],
    'age': [5, 19, 20, 14]
}

# Create a DataFrame from the dictionary of student data
students = pd.DataFrame(data)
# Call the function to drop rows with missing names from the DataFrame
result = dropMissingData(students)
# Print the DataFrame with missing names removed
print(result)
