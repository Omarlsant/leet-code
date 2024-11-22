# 2882. Drop Duplicate Rows
import pandas as pd  # Importing: pandas library for data manipulation

def dropDuplicateEmails(customers: pd.DataFrame) -> pd.DataFrame:
    # The dropDuplicateEmails function receives a pandas DataFrame called 'customers'
    # Drop duplicate rows based on the 'email' column, keeping the first occurrence
    unique_customers = customers.drop_duplicates(subset='email', keep='first')
    # Return the DataFrame with duplicate emails removed
    return unique_customers

# Define a dictionary with customer data
data = {
    'customer_id': [1, 2, 3, 4, 5, 6],
    'name': ['Ella', 'David', 'Zachary', 'Alice', 'Finn', 'Violet'],
    'email': ['emily@example.com', 'michael@example.com', 'sarah@example.com', 'john@example.com', 'john@example.com', 'alice@example.com']
}

# Create a DataFrame from the dictionary of customer data
customers = pd.DataFrame(data)
# Call the function to drop duplicate emails from the DataFrame
result = dropDuplicateEmails(customers)
# Print the DataFrame with duplicate emails removed
print(result)
