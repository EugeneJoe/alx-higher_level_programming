#!/bin/bash
# Takes in a URL and displays all HTTP methods the server will accept
curl -s -X --request OPTIONS "$1" -i | grep Allow: | cut -d ' ' -f 2-
