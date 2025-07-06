#!/usr/bin/python3
"""
Reddit API Subreddit Subscriber Counter

This module provides functionality to query the Reddit API and retrieve
the number of subscribers for a given subreddit.

Functions:
    number_of_subscribers(subreddit): Returns subscriber count for a subreddit

Example:
    >>> from subs import number_of_subscribers
    >>> count = number_of_subscribers("python")
    >>> print(f"Python subreddit has {count} subscribers")

Author: temp_user
Version: 1.0
"""

import requests


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers
    for a given subreddit.
    
    This function makes an HTTP GET request to Reddit's JSON API endpoint
    for subreddit information. It handles invalid subreddits, network errors,
    and API response errors gracefully.
    
    Args:
        subreddit (str): The name of the subreddit (without 'r/' prefix)
        
    Returns:
        int: Number of subscribers for the subreddit, or 0 if:
             - Subreddit doesn't exist
             - Subreddit is private
             - Network error occurs
             - Invalid input provided
             
    Example:
        >>> number_of_subscribers("python")
        892345
        >>> number_of_subscribers("nonexistent_subreddit")
        0
    """
    if not subreddit or not isinstance(subreddit, str):
        return 0
    
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {
        'User-Agent': 'python:subreddit.subscriber.counter:v1.0 (by /u/temp_user)'
    }
    
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        
        if response.status_code == 200:
            data = response.json()
            return data['data']['subscribers']
        else:
            return 0
    except (requests.RequestException, KeyError, ValueError):
        return 0
