# 2889. Reshape Data: Pivot
import pandas as pd  # Importing: pandas library for data manipulation

def pivotTable(weather: pd.DataFrame) -> pd.DataFrame:
    # The pivotTable function receives a pandas DataFrame called 'weather'
    # Pivot the table so that each row represents temperatures for a specific month,
    # and each city is a separate column
    return weather.pivot(index='month', columns='city', values='temperature')

# Define a dictionary with weather data
data = {
    'city': ['Jacksonville', 'Jacksonville', 'Jacksonville', 'Jacksonville', 'Jacksonville', 'ElPaso', 'ElPaso', 'ElPaso', 'ElPaso', 'ElPaso'],
    'month': ['January', 'February', 'March', 'April', 'May', 'January', 'February', 'March', 'April', 'May'],
    'temperature': [13, 23, 38, 5, 34, 20, 6, 26, 2, 43]
}

# Create a DataFrame from the dictionary of weather data
weather = pd.DataFrame(data)
# Call the function to pivot the table
result = pivotTable(weather)
# Print the pivoted DataFrame
print(result)
