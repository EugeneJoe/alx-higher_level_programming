#!/usr/bin/python3
"""
fetches https://intranet.hbtn.io/status
"""

import requests

if __name__ == "__main__":
    resp = requests.get("https://intranet.hbtn.io/status")
    print("Body Response:")
    print("\t- type: {}".format(type(resp.text)))
    print("\t- content: {}".format(resp.text))
