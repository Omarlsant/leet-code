# 2883. Drop Missing Data
import pandas as pd

def dropMissingData(students: pd.DataFrame) -> pd.Dataframe:
    cleaned_students = students.dropna(subset=['name'])
    return cleaned_students

data = {
    'student_id': [32, 217, 779, 849],
    'name': ['Piper', None, 'Georgia', 'Willow'],
    'age': [5, 19, 20, 14]
}

students = pd.DataFrame(data)
result = dropMissingData(students)
print(result)