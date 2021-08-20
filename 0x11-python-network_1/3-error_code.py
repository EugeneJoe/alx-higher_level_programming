#!/usr/bin/python3
"""
 Takes in a URL, sends a request to the URL and displays the
 body of the response (decoded in utf-8)
"""

import urllib.request as request
import urllib.parse as parse
from urllib.error import HTTPError
from sys import argv

if __name__ == "__main__":
    try:
        with request.urlopen(argv[1]) as reply:
            html = reply.read()
            print("{}".format(html.decode('utf-8')))
    except HTTPError as e:
        print("Error code: {}".format(e.code))
