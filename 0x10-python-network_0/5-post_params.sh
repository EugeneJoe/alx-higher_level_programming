
#!/bin/bash
# Takes a URL, sends a POST request to it and displays the body of the response
# send a variable email with the value hr@holbertonschool.com
# send a variable subject with the value I will always be here for PLD
curl -s -X POST -d "email=hr@holbertonschool.com" -d "subject=I will \
always be here for PLD" "$1"
