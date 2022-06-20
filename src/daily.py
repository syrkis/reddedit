# daily.py
#   daily.py is a script that will run daily
# by: Noah Syrkis

import src.utils as utils
from datetime import datetime, timedelta
import pandas as pd
import random, time

def run_daily(client, df, count=100):
    post_iter = utils.get_new_posts(client, count*2)
    df        = add_new_posts_and_log_votes(post_iter, df, count, client)
    return df

def add_new_posts_and_log_votes(post_iter, df, count, client):
    today     = datetime.now().strftime("%Y-%m-%d")
    posts = []

    # add new posts
    while len(posts) < count:
        post = next(post_iter)
        if post.id not in df.index and post.score == 1:
            posts.append((post.id, post.score, 0))
        time.sleep(.1)
    random.shuffle(posts)

    # upvote posts in treatment group
    for i in range(len(posts)//2):
        posts[i] = (posts[i][0], posts[i][1] + 1, 1) # we're including OUR vote
        utils.upvote_post(client, posts[i][0])
        time.sleep(.1)
    posts.sort()

    # add new posts to dataframe
    for post, score, treatment in posts:
        sample = pd.DataFrame([[post, treatment]],
                columns=['post_id', 'treatment'])
        sample.set_index('post_id', inplace=True)
        df = pd.concat([df, sample])

    for post in df.index:
        df[today].loc[post] = utils.get_likes(client, post)
        time.sleep(.1)
    return df

