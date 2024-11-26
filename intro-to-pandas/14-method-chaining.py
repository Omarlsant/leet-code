# 2891. Method Chaining
import pandas as pd  # Importing: pandas library for data manipulation

def findHeavyAnimals(animals: pd.DataFrame) -> pd.DataFrame:
    # Filter animals weighing more than 100 kg, sort by weight in descending order, and select the 'name' column
    return animals[animals['weight'] > 100].sort_values(by='weight', ascending=False)[['name']]

# Define a dictionary with animal data
data = {
    'name': ['Tatiana', 'Khaled', 'Alex', 'Jonathan', 'Stefan', 'Tommy'],
    'species': ['Snake', 'Giraffe', 'Leopard', 'Monkey', 'Bear', 'Panda'],
    'age': [98, 50, 6, 45, 100, 26],
    'weight': [464, 41, 328, 463, 50, 349]
}

# Create a DataFrame from the dictionary of animal data
animals = pd.DataFrame(data)
# Call the function to find heavy animals
result = findHeavyAnimals(animals)
# Print the names of heavy animals
print(result)
