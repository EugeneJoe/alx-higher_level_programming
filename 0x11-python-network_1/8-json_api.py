#!/usr/bin/python3
"""
Takes in a letter and sends a POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter
"""
import requests
from sys import argv

if __name__ == "__main__":
    if len(argv) > 1:
        payload = {'q': argv[1]}
    else:
        payload = {'q': ""}
    resp = requests.post("http://0.0.0.0:5000/search_user", data=payload)
    try:
        json = resp.json()
        if json == {}:
            print("No result")
        else:
            print("[{}] {}".format(json['id'], json['name']))
    except ValueError:
        print("Not a valid JSON")
