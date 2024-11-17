# 2880. Select Data
import pandas as pd

def selectData(students: pd.DataFrame) -> pd.DataFrame:
    selected_student = students[students['student_id'] == 101]
    result = selected_student[['name', 'age']]
    return result

data = {
    'student_id': [101, 53, 128, 3],
    'name': ['Ulysses', 'William', 'Henry', 'Henry'],
    'age': [13, 10, 6, 11]
}

students = pd.DataFrame(data)
result = selectData(students)
print(result)
