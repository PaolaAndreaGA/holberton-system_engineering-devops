#!/usr/bin/python3
""" Returns the number of subscribers (not active users, total subscribers)
for a given subreddit. If an invalid subreddit is given,
the function should return 0.
"""
import requests


def number_of_subscribers(subreddit):
    """returns the number of subscribers for a given subreddit"""

    url = 'http://www.reddit.com/r/' + subreddit + '/about.json'
    try:
        req = requests.get(url,
                           headers={'User-Agent': 'My User Agent 1.0'},
                           allow_redirects=False).json()
        return req['data'].get('subscribers')
    except Exception:
        return 0
