#!/usr/bin/python3
"""
Takes repository name and owner name and then prints
latest 10 commits
"""

import sys
import requests

if __name__ == '__main__':
    reposit = sys.argv[1]
    owner = sys.argv[2]

    url = 'https://api.github.com/repos/{}/{}/commits'.format(owner, reposit)
    request = requests.get(url)
    res = request.json()
    try:
        for i in range(10):
            print('{}: {}'.format(
                res[i].get('sha'),
                res[i].get('commit').get('author').get('name')))
    except IndexError:
        pass
