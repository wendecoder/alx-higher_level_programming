#!/usr/bin/python3
"""
sends a POST request to the passed URL with
the email as a parameter, and displays
the body of the response (decoded in utf-8)
"""

import urllib.request
import sys

if __name__ == '__main__':
    url = sys.argv[1]
    email = sys.argv[2]
    email = email.encode('ascii')

    request = urllib.request.Request(url, email)
    with urllib.request.urlopen(request) as Response:
        print(Response.read().decode('UTF-8'))
