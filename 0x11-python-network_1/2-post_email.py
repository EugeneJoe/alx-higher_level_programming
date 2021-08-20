#!/usr/bin/python3
"""
Takes in a URL and an email, sends a POST request to the URL with the email as
a parameter and displays the body of the response decoded in utf-8
"""
import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    data = urllib.parse.urlencode({'email': sys.argv[2]}).encode('ascii')
    req = urllib.request.Request(sys.argv[1], data)
    with urllib.request.urlopen(req) as reply:
        html = reply.read()
        print('{}'.format(html.decode('utf-8')))
