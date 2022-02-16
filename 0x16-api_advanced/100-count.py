#!/usr/bin/python3
"""recursive function that queries the Reddit API,
parses the title of all hot articles
"""
import requests


def count_words(subreddit, word_list):
    """Searches for keywords in hot titles"""
    URL = 'https://www.reddit.com/r/' + subreddit + '/hot.json'
    headers = {'User-agent': 'My User Agent 4.0'}
    try:
        req = requests.get(URL, headers=headers)
        request_data = req.json()
    except Exception:
        return None
