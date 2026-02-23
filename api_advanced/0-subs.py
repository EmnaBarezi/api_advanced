#!/usr/bin/python3
"""
Returns number of subscribers for a subreddit
"""

import requests


def number_of_subscribers(subreddit):
    """
    Queries Reddit API and returns subscriber count
    """

    if subreddit is None:
        return 0

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)

    headers = {
        "User-Agent": "ALU-Project-Agent"
    }

    try:
        response = requests.get(
            url,
            headers=headers,
            allow_redirects=False,
            timeout=10
        )

        if response.status_code != 200:
            return 0

        return response.json().get("data", {}).get("subscribers", 0)

    except Exception:
        return 0
