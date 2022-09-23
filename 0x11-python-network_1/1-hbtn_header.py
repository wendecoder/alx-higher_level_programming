#!/usr/bin/python3
"""
sends request to the url from argument
and display the value of the header
X-Request-Id from response
"""

import urllib.request
import sys

if __name__ == '__main__':
    url = sys.argv[1]
    request = urllib.request.Request(url)
    with urllib.request.urlopen(request) as Response:
        print(dict(Response.headers)['X-Request-Id'])
