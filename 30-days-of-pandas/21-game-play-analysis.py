# 511. Game Play Analysis I
import pandas as pd

def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    # Group by player_id and find the minimum event_date for each player
    first_login = activity.groupby('player_id')['event_date'].min().reset_index()
    
    # Rename the column for the result
    first_login.rename(columns={'event_date': 'first_login'}, inplace=True)
    
    return first_login
