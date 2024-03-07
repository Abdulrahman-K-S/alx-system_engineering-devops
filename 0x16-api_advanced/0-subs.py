#!/usr/bin/python3
"""Queries the Reddit API and
returns the number of subscribers
(not active users, total subscribers)
for a given subreddit.

If an invalid subreddit is given,
the function should return 0.
"""
import requests


def number_of_subscribers(subreddit):
    """Returns the total number of subscribers
    for a given subreddit.
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/Imanolasolo)"
    }
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 404:
        return 0
    results = response.json().get("data")
    return results.get("subscribers")
