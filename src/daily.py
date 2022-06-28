# daily.py
#   daily.py is a script that will run daily
# by: Noah Syrkis

import src.utils as utils
from datetime import datetime, timedelta
from prawcore.exceptions import NotFound, Forbidden, PrawcoreException
from praw.exceptions import PRAWException
import pandas as pd
import random, time
from tqdm import tqdm

def run_daily(client, df, count=100):
    alpha = 3
    posts   = []
    fuckups = 0
    stream  = utils.get_stream(client)
    while True:
        try:
            for submission in stream:
                if len(posts) < count * alpha:
                    posts.append(submission)
                    time.sleep(.08)
                else:
                    break
        except (PrawcoreException, PRAWException) as err:
            print('stream fuckup')
        except Exception as e:
            fuckups += 1
            print('script fuckup', fuckups, e)
        if len(posts) >= count * alpha:
            break
        time.sleep(.1)
    df        = add_new_posts_and_log_votes(posts, df, count, client)
    return df

def add_new_posts_and_log_votes(stream, df, count, client):
    today     = datetime.now().strftime("%Y-%m-%d")
    posts     = []

    # add new posts
    for post in stream:
        time.sleep(.1)
        if len(posts) >= count:
            break
        if post.id not in df.index and post.score == 1:
            posts.append((post.id, post.score, 0)) # 0 is for treatment/control
    random.shuffle(posts)

    # upvote posts in treatment group
    for i in range(len(posts)//2):
        posts[i] = (posts[i][0], posts[i][1] + 1, 1) # including OUR vote
        utils.upvote_post(client, posts[i][0])
        time.sleep(.1)
    posts.sort()

    # add new posts to dataframe
    for post, score, treatment in posts:
        sample = pd.DataFrame([[post, treatment]],
                columns=['post_id', 'treatment'])
        sample.set_index('post_id', inplace=True)
        df = pd.concat([df, sample])

    for post in tqdm(df.index):
        try:
            df[today].loc[post] = int(utils.get_likes(client, post))
            time.sleep(.1)
        except NotFound:
            df[today].loc[post] = "not found"
        except Forbidden:
            df[today].loc[post] = "forbidden"
    return df

