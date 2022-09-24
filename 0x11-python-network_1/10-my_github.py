#!/usr/bin/python3
"""
takes your GitHub credentials
(username and password) and
uses the GitHub API to display your id
"""

import requests
import sys
from requests.auth import HTTPBasicAuth

if __name__ == '__main__':

    user = sys.argv[1]
    passw = sys.argv[2]

    auth = HTTPBasicAuth(user, passw)
    response = requests.get("https://api.github.com/user", auth=auth)
    print(response.json().get('id'))
