
#!/bin/bash
# Takes a URL and sends a DELETE request to it and displays the body
# of the response

curl -s -X DELETE "$1"
