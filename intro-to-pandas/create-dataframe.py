# 2877. Create a DataFrame from List
import pandas as pd # Importing: pandas library
from typing import List # Importing: List from typing

def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:
    # Create a Dataframe from a list (student_data)
    df = pd.DataFrame(student_data, columns = ['student_id', 'age'])
    return df # Returns the created DataFrame

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