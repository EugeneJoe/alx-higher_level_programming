#!/usr/bin/python3
"""
Lists 10 commits (from the most recent to oldest) of a repository
Accepts repository name and owner name
"""
import requests
from sys import argv

if __name__ == "__main__":
    u = 'https://api.github.com/repos/' + argv[2] + '/' + argv[1] + '/commits'
    resp = requests.get(u)
    json = resp.json()
    for i in range(0, 10):
        print("{}: {}".format(json[i].get('sha'),
                              json[i].get('commit').get('author').get('name')))
