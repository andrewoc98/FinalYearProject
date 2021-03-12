import os
import pandas as pd

for filename in os.listdir('../TweetModel/TweetFolder/'):
    print(filename)
    if filename.endswith('Tweet.csv'):
            df = pd.read_csv(f'../TweetModel/TweetFolder/{filename}')