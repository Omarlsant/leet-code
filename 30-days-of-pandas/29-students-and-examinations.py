# 1280. Students and Examinations
import pandas as pd

def students_and_examinations(students: pd.DataFrame, subjects: pd.DataFrame, examinations: pd.DataFrame) -> pd.DataFrame:
    # Create a cross join between students and subjects to ensure every student is paired with every subject
    cross_join = pd.merge(students, subjects, how='cross').sort_values(by=['student_id', 'subject_name'])
    # Group by student_id and subject_name, then count the number of attended exams
    exam_counts = examinations.groupby(['student_id', 'subject_name']).agg(attended_exams=('subject_name', 'count')).reset_index()
    # Merge the cross join result with the exam counts
    result = pd.merge(cross_join, exam_counts, how='left', on=['student_id', 'subject_name'])
    # Fill NaN values in 'attended_exams' with 0
    result['attended_exams'] = result['attended_exams'].fillna(0).astype(int)
    # Select the columns we need
    result = result[['student_id', 'student_name', 'subject_name', 'attended_exams']]
    
    return result
