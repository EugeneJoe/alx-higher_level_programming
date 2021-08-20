#!/bin/bash
# Takes a URL and a JSON filename, and sends a POST request to the URL
# sending the file contents to the URL, and displaying the
# body of the response

curl -s -X POST -H "Content-Type: application/json" -d @"$2" "$1"
