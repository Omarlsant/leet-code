# 2880. Select Data
import pandas as pd  # Importing: pandas library for data manipulation

def selectData(students: pd.DataFrame) -> pd.DataFrame:
    # The selectData function receives a pandas DataFrame called 'students'
    # Select the row where 'student_id' is 101
    selected_student = students[students['student_id'] == 101]
    # Extract only the 'name' and 'age' columns from the selected row
    result = selected_student[['name', 'age']]
    # Return the result which contains the 'name' and 'age' columns of the selected student
    return result

# Define a dictionary with student data
data = {
    'student_id': [101, 53, 128, 3],
    'name': ['Ulysses', 'William', 'Henry', 'Henry'],
    'age': [13, 10, 6, 11]
}

# Create a DataFrame from the dictionary of student data
students = pd.DataFrame(data)
# Call the function to select the data of the student with 'student_id' 101
result = selectData(students)
# Print the selected data with the 'name' and 'age' columns of the student
print(result)
