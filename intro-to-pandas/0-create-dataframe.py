# 2877. Create a DataFrame from List
from typing import List  # Importing: List from typing
import pandas as pd  # Importing: pandas library

def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:
    # Create a DataFrame from a list (student_data)
    df = pd.DataFrame(student_data, columns=['student_id', 'age'])
    # Returns the created DataFrame
    return df

# Defining a list (student_data) with student_id and age
student_data = [
    [1, 15],
    [2, 11],
    [3, 11],
    [4, 20]
]

# Calling the function createDataframe with student_data as an argument
df = createDataframe(student_data)

# Printing the DataFrame
print(df)
