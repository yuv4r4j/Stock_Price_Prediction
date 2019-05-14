import os
import pandas as pd
import sys


folder_path = os.path.join(os.path.join('src', 'data'), 'twitter_feeds')
feed_file_path = os.listdir(folder_path)

dfs = [
    pd.read_csv(os.path.join(folder_path, x), encoding='utf-8') for x in feed_file_path
    if os.path.isfile(os.path.join(folder_path, x))
]

df = pd.concat(dfs)
df.write_csv('test.csv')
