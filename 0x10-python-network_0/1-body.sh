#!/bin/bash
# Takes a URL, sends a GET request to it and display the body of the response
# only if the status code is 200

# store the whole response with the status at the and
HTTP_RESPONSE=$(curl --write-out "HTTPSTATUS:%{http_code}" -s -X GET -L "$1")

# extract the body
HTTP_BODY=${HTTP_RESPONSE//HTTPSTATUS:*/''}

# extract the status
HTTP_STATUS=$(echo "$HTTP_RESPONSE" | tr -d '\n' | sed -e 's/.*HTTPSTATUS://')

# example using the status
if [  "$HTTP_STATUS" -eq 200  ]; then
     echo -n "$HTTP_BODY"
     exit 1
fi
