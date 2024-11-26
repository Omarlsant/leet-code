# 2886. Change Data Type
import pandas as pd  # Importing the pandas library for data manipulation.

def changeDatatype(students: pd.DataFrame) -> pd.DataFrame:
    # Converts the 'grade' column in the DataFrame to integer type.
    students['grade'] = students['grade'].astype(int)
    return students  # Returns the modified DataFrame.
