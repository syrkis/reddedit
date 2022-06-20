# utils.py
#   Utility functions for the project.
# by: Noah Syrkis

# imports
import numpy as np
import pandas as pd
import praw, yaml, os
from datetime import datetime, timedelta


# login to reddit
def get_client():
    with open('.env.yaml') as f:
        env = yaml.safe_load(f)['env']
    print(env)
    exit()
    client = praw.Reddit(client_id=env['client_id'],
                         client_secret=env['secret'],
                         username=env['username'],
                         password=env['password'],
                         user_agent=env['agent'])
    return client

# get subreddit
def get_new_posts(client, subreddit, num_posts):
    # get new posts
    new_posts = client.subreddit(subreddit).new(limit=num_posts)
    return new_posts

def upvote_post(post):
    submission = reddit.submission(post)
    submission.upvote()

def get_likes(post):
    submission = reddit.submission(post)
    return submission.likes # fix to look at 

def setup():
    if not os.path.isfile('data.csv'):
        today = datetime.today()
        cols  = ['post_id', 'like_count', 'like_ratio']
        dates = [date_to_str(today + timedelta(days=x)) for x in range(30)]
        df = pd.DataFrame(columns=cols + dates)
        df.to_csv('data.csv', index=False)
    else :
        df = pd.read_csv('data.csv')
    return df

def date_to_str(date):
    return date.strftime('%Y-%m-%d')

