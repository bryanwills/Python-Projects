import praw
import requests
import pandas as pd
from praw.models import MoreComments
from bs4 import BeautifulSoup as bs

posts = []

reddit = praw.Reddit(client_id='b9IU23fy4c4K6g', client_secret='GqGmn8Rgge9r7IQ-jRczYVy_f0I', user_agent='testapplication')

ml_subreddit = reddit.subreddit('MachineLearning')

#hot_posts = reddit.subreddit('MachineLearning').hot(limit=25)
#for post in hot_posts:
    #print(post.title) 

for post in ml_subreddit.hot(limit=25):
    posts.append([post.title, post.score, post.id, post.subreddit, post.url, post.num_comments, post.selftext, post.created])
posts = pd.DataFrame(posts,columns=['title', 'score', 'id', 'subreddit', 'url', 'num_comments', 'body', 'created'])
print(posts)
print(ml_subreddit.description)

submission = reddit.submission(url="https://www.reddit.com/r/MapPorn/comments/a3p0uq/an_image_of_gps_tracking_of_multiple_wolves_in/")
for top_level_comment in submission.comments:
    if isinstance(top_level_comment, MoreComments):
        continue
    print(top_level_comment.body)

submission.comments.replace_more(limit=0)
for comment in submission.comments.list():
    print(comment.body)
