# 1527. Patients With a Condition
import pandas as pd

def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    # Split the 'conditions' column into lists of conditions
    patients['conditions_list'] = patients['conditions'].str.split()
    # Check if any condition in the list starts with 'DIAB1'
    patients['has_diab1'] = patients['conditions_list'].apply(lambda x: any(cond.startswith('DIAB1') for cond in x) if x else False)
    # Filter the DataFrame to keep only rows with 'DIAB1' conditions
    result = patients[patients['has_diab1']].drop(columns=['conditions_list', 'has_diab1'])

    return result
