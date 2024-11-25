# 2890. Reshape Data: Melt
import pandas as pd  # Importing: pandas library for data manipulation

def meltTable(report: pd.DataFrame) -> pd.DataFrame:
    # Reshape the data so that each row represents sales data for a product in a specific quarter
    return report.melt(id_vars=['product'], var_name='quarter', value_name='sales')

# Define a dictionary with report data
data = {
    'product': ['Umbrella', 'SleepingBag'],
    'quarter_1': [417, 800],
    'quarter_2': [224, 936],
    'quarter_3': [379, 93],
    'quarter_4': [611, 875]
}

# Create a DataFrame from the dictionary of report data
report = pd.DataFrame(data)
# Call the function to melt the table
result = meltTable(report)
# Print the reshaped DataFrame
print(result)
