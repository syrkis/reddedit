# utils.py
#   Utility functions for the project.
# by: Noah Syrkis

# imports
import pandas as pd
import praw, os
from datetime import datetime, timedelta


# login to reddit
def get_client():
    client = praw.Reddit(client_id=os.getenv('REDDIT_CLIENT'),
                         client_secret=os.getenv('REDDIT_SECRET'),
                         username='syrkis',
                         password=os.getenv('REDDIT_PASSWORD'),
                         user_agent='syrkis')
    return client

def get_stream(client):
    stream = client.subreddit('wallstreetbets').stream.submissions()
    return stream

def upvote_post(client, post):
    submission = client.submission(post)
    submission.upvote()

def get_likes(client, post):
    submission = client.submission(post)
    return submission.score # fix to look at 

def setup(path):
    if not os.path.isfile(path):
        today = datetime.today()
        cols  = ['post_id', 'treatment']
        dates = [date_to_str(today + timedelta(days=x)) for x in range(30)]
        df = pd.DataFrame(columns=cols + dates)
        df.set_index('post_id', inplace=True)
        df.to_csv(path)
    else :
        df = pd.read_csv(path)
        df.set_index('post_id', inplace=True)
    return df

def date_to_str(date):
    return date.strftime('%Y-%m-%d')

