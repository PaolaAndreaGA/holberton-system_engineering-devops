#!/usr/bin/python3
"""function that queries the Reddit API and prints the titles
of the first 10 hot posts listed for a given subreddit.
"""
import requests


def top_ten(subreddit):
    """queries the Reddit API and prints
    the titles of the first 10 hot posts
    """
    URL = 'https://www.reddit.com/r/' + subreddit + '/hot.json'
    params = {'limit': 10}
    headers = {'User-agent': 'My User Agent 2.0'}
    try:
        req = requests.get(URL,
                           headers=headers,
                           params=params,
                           allow_redirects=False).json()
        data = req['data']['children']
        for listing in data:
            title = listing.get('data').get('title')
            print(title)
    except Exception:
        print('None')
