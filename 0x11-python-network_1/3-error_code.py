#!/usr/bin/python3
"""
sends a request to the passed URL and displays
the body of the response (decoded in utf-8) while
managing the error exception using urllib.error.HTTPError
"""

import urllib
import sys

if __name__ == '__main__':
    url = sys.argv[1]
    request = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(request) as Response:
            print(Response.read().decode('UTF-8'))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
    except:
        pass
