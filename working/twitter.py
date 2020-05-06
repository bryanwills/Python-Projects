import tweepy
import time

auth = tweepy.OAuthHandler('YWoU4xGj6qZgaXgLL8To2IiLZ',
                           'EQU9UPfww8YfB0lM2Nclsj1AJ5e2jFYp0wJXxJqyCOY6t85tF4')

auth.set_access_token('1225891109836115968-4LrEY3qpldNWno3qK44FIWQ2udN3RS',
                      'j2B76Ga0WkqfLjIK0618SH9h4wPEfRQcG1F5TLoNiF4F6')

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

user = api.me()

for follower in tweepy.Cursor
