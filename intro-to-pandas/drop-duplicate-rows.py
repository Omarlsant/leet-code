# 2882. Drop Duplicate Rows
import pandas as pd

def dropDuplicateEmails(customers: pd.DataFrame) -> pd.DataFrame:
    unique_customers = customers.drop_duplicates(subset='email', keep='first')
    return unique_customers

data = {
    'customer_id': [1, 2, 3, 4, 5, 6],
    'name': ['Ella', 'David', 'Zachary', 'Alice', 'Finn', 'Violet'],
    'email': ['emily@example.com', 'michael@example.com', 'sarah@example.com', 'john@example.com', 'john@example.com', 'alice@example.com']
}

customers = pd.DataFrame(data)
result = dropDuplicateEmails(customers)
print(result)