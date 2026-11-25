#!/bin/bash
# Send the exercise email and subject as POST form fields.
curl -s --data-urlencode 'email=test@gmail.com' --data-urlencode 'subject=I will always be here for PLD' -- "$1"
