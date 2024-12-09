# 1683. Invalid Tweets
import pandas as pd

def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    # Filter tweets with content longer than 15 characters
    invalid_tweets_df = tweets[tweets['content'].str.len() > 15]
    # Select only the tweet_id column
    result = invalid_tweets_df[['tweet_id']]
    
    return result

