#!/usr/bin/python3
"""
 sends a request to the passed URL
 and displays the body of the response.
"""

import requests
import sys

if __name__ == '__main__':
    url = sys.argv[1]
    try:
        response = requests.get(url)
        print(response.text)
        response.raise_for_status()
    except requests.exceptions.HTTPError as e:
        print("Error code: {}".format(e.code)
