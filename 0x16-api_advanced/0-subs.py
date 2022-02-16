#!/usr/bin/python3
""" Returns the number of subscribers (not active users, total subscribers)
for a given subreddit. If an invalid subreddit is given,
the function should return 0.
"""
import requests


def number_of_subscribers(subreddit):
    """returns the number of subscribers for a given subreddit"""

    URL = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    try:
        req = requests.get(URL,
                           headers={'User-Agent': 'My User Agent 1.0'},
                           allow_redirects=False).json()
        return req['data'].get('subscribers')
    except Exception:
        return 0
