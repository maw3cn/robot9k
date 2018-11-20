import praw
import os

reddit = praw.Reddit(client_id=os.environ['REDDIT_CLIENT_ID'],
                     client_secret=os.environ['REDDIT_CLIENT_SECRET'],
                     username=os.environ['REDDIT_USERNAME'],
                     password=os.environ['REDDIT_PASSWORD'],
                     user_agent='Redbot9k:v0.1')

subreddit = reddit.subreddit('askreddit')

for comment in subreddit.stream.comments():
    print(comment.id, comment.body, '\nParent: ', comment.parent_id, '\n---')
