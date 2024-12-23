# 1050. Actors and Directors Who Cooperated At Least Three Times
import pandas as pd

def actors_and_directors(actor_director: pd.DataFrame) -> pd.DataFrame:
    # Group by actor_id and director_id, then count the number of occurrences
    counts = actor_director.groupby(['actor_id', 'director_id']).size().reset_index(name='count')
    # Filter the pairs where the count is at least 3
    result = counts[counts['count'] >= 3][['actor_id', 'director_id']]
    
    return result
