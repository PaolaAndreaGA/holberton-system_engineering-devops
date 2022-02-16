#!/usr/bin/python3
"""recursive function that queries the Reddit API,
parses the title of all hot articles
"""
import requests


def count_words(subreddit, word_list):
    """Searches for keywords in hot titles"""
    URL = 'https://www.reddit.com/r/' + subreddit + '/hot.json'
    headers = {'User-agent': 'My User Agent 4.0'}
    req = requests.get(URL, headers=headers)
    if req.status_code != 200:
        return(None)
    request_data = req.json()
