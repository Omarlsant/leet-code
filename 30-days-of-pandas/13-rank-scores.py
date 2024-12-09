# 178. Rank scores.
import pandas as pd

def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    # Sort the scores in descending order
    scores = scores.sort_values(by='score', ascending=False)
    # Rank the scores with method 'dense' to ensure no holes in the ranking
    scores['rank'] = scores['score'].rank(method='dense', ascending=False).astype(int)
    # Select the relevant columns for the final result
    result = scores[['score', 'rank']]
    
    return result
