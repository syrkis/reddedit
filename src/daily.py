# daily.py
#   daily.py is a script that will run daily
# by: Noah Syrkis

import src.utils as utils

def run_daily(client, data):
    return data
    posts = []
    post_iter = utils.get_new_posts(client, "wallstreetbets", 10)
    for post in post_iter:
        posts.append(post)
