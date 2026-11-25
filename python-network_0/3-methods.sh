#!/bin/bash
# Display the server's allowed methods from its OPTIONS response.
curl -s -X OPTIONS -D - -o /dev/null -- "$1" | awk 'tolower($1) == "allow:" { sub(/^[^:]*:[[:space:]]*/, ""); sub(/\r$/, ""); print }'
