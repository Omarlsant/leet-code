# 1148. Article Views
import pandas as pd  # Import pandas library for data manipulation.

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    self_views = views[views['author_id'] == views['viewer_id']]  
    # Filter rows where the author viewed their own article.
    result = self_views[['author_id']].drop_duplicates().rename(columns={'author_id': 'id'}).sort_values('id')  
    # Select unique author IDs, rename the column to 'id', and sort by 'id'.

    return result  
    # Return the resulting DataFrame with authors who viewed their own articles.
