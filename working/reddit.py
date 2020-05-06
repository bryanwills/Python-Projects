import praw
import requests
from bs4 import BeautifulSoup as bs

reddit = praw.Reddit(client_id='b9IU23fy4c4K6g', client_secret='GqGmn8Rgge9r7IQ-jRczYVy_f0I', user_agent='testapplication')

hot_posts = reddit.subreddit('MachineLearning').hot(limit=25)
for post in hot_posts:
    print(post.title) 
