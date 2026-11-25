#!/bin/bash
# Send the exercise user ID in a GET request.
curl -s -H 'X-HolbertonSchool-User-Id: 98' -- "$1"
