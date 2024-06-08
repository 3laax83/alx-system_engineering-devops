#!/usr/bin/python3
"""
a function that queries the Reddit API and prints the titles of the
first 10 hot posts listed for a given subreddit.
"""

import requests


def top_ten(subreddit):
    """
    main function
    """
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    hdrs = {"User-Agent": "Custom"}
    res = requests.get(url, allow_redirects=False, headers=hdrs).json()
    try:
        for p in res.get("data").get("children"):
            print(p.get("data").get("title"))
    except Exception:
        print(None)
