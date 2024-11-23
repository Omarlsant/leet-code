# 2888. Reshape Data: Concatenate
import pandas as pd # Importing the pandas library for data manipulation.

def concatenateTables(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
    # Concatenate df1 and df2 vertically using the pd.concat() function
    result = pd.concat([df1, df2], ignore_index=True)
    return result

# Define two DataFrames
df1 = pd.DataFrame({
    'student_id': [1, 2, 3, 4],
    'name': ['Mason', 'Ava', 'Taylor', 'Georgia'],
    'age': [8, 6, 15, 17]
})

df2 = pd.DataFrame({
    'student_id': [5, 6],
    'name': ['Leo', 'Alex'],
    'age': [7, 7]
})

# Apply the function to the DataFrames
concatenated_df = concatenateTables(df1, df2)
print(concatenated_df)
