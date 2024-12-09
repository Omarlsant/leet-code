# 184. Department Highest Salary
import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    # Merge employee and department tables on departmentId
    merged = employee.merge(department, left_on='departmentId', right_on='id', suffixes=('_employee', '_department'))
    # Group by department and find the maximum salary in each department
    max_salaries = merged.groupby('name_department')['salary'].max().reset_index()
    # Merge the max salaries with the original merged dataframe to get the highest paid employees in each department
    result = merged.merge(max_salaries, on=['name_department', 'salary'])
    # Select the relevant columns for the final result
    result = result[['name_department', 'name_employee', 'salary']]
    # Rename the columns as required
    result.columns = ['Department', 'Employee', 'Salary']
    
    return result

