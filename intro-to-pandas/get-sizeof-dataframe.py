# 2878. Get the Size of a DataFrame
from typing import List  # Import List from the typing library for type annotation
import pandas as pd  # Import pandas library for data manipulation

def getDataframeSize(players: pd.DataFrame) -> List[int]:
    # The getDataframeSize function receives a pandas DataFrame called 'players'
    # Get the number of rows and columns of the DataFrame
    rows, cols = players.shape
    # Return a list with the number of rows and columns
    return [rows, cols]

# Define a dictionary with player data
data = {
    'player_id': [846, 749, 155, 583, 388, 883, 355, 247, 761, 642],
    'name': ['Mason', 'Riley', 'Bob', 'Isabella', 'Zachary', 'Ava', 'Violet', 'Thomas', 'Jack', 'Charlie'],
    'age': [21, 30, 28, 32, 24, 23, 18, 27, 33, 36],
    'position': ['Forward', 'Winger', 'Striker', 'Goalkeeper', 'Midfielder', 'Defender', 'Striker', 'Striker', 'Midfielder', 'Center-back'],
    'team': ['RealMadrid', 'Barcelona', 'ManchesterUnited', 'Liverpool', 'BayernMunich', 'Chelsea', 'Juventus', 'ParisSaint-Germain', 'ManchesterCity', 'Arsenal']
}

# Create a DataFrame from the dictionary of player data
players = pd.DataFrame(data)
# Call the function to get the size of the DataFrame
size = getDataframeSize(players)
# Print the size of the DataFrame (number of rows and columns)
print(size)
