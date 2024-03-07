#!/usr/bin/python3
"""Function to query subscribers on a given Reddit subreddit."""
import requests


def number_of_subscribers(subreddit):
    """Return the total number of subscribers on a given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {
        "User-Agent": "python:reddit_subscribers:v1.0.0 (by /u/AbdulrahmanKamel)"
    }

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json().get("data")
            return data.get("subscribers", 0)
        else:
            return 0
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return 0