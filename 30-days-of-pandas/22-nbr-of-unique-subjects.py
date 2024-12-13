# 2356. Number of Unique Subjects for Each Teacher
import pandas as pd

def count_unique_subjects(teacher: pd.DataFrame) -> pd.DataFrame:
    # Select only the necessary columns and drop duplicates to ensure unique subject counts
    unique_subjects = teacher[['teacher_id', 'subject_id']].drop_duplicates()
    # Group by teacher_id and count the number of unique subjects
    result = unique_subjects.groupby('teacher_id').size().reset_index(name='cnt')
    
    return result
