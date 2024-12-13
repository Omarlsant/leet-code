# 596. Classes More Than 5 Students
import pandas as pd

def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    # Group by 'class' and count the number of students in each class
    class_counts = courses.groupby('class').size().reset_index(name='student_count')
    # Filter classes that have at least 5 students
    result = class_counts[class_counts['student_count'] >= 5]
    # Select only the 'class' column for the result
    result = result[['class']]
    
    return result
