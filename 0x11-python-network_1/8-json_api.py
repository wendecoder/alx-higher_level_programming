#!/usr/bin/python3
"""
sends a POST request to
http://0.0.0.0:5000/search_user 
with the letter as a parameter.
"""

import requests
import sys

if __name__ == '__main__':
    if len(sys.argv) < 2:
        letter = ""
        search_letter = {'q': letter}
    else:
        letter = sys.argv[1]
        search_letter = {'q': letter}

    url = 'http://0.0.0.0:5000/search_user'
    response = requests.post(url,search_letter)
    try:
        response = response.json()
        if response == {}:
            print("No result")
        else:
            print("[{}] {}".format(response['id'], response['name']))
    except ValueError:
        print("Not a valid JSON")
