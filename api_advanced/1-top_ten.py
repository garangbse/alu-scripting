#!/usr/bin/python3
""" top_ten.py """
import requests


def top_ten(subreddit):
    """ prints the titles of the first 10 hot posts listed in a subreddit """
    url = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)
    headers = {'User-Agent': 'MyAPI/0.0.1'}
    response = requests.get(subreddit_url, headers=headers)

    # print(response)
    if response.status_code == 200:
        json_data = response.json()
        for i in range(10):
            print(json_data.get('data').get('children')[i].get('data').get('title'))
        else: print(None)