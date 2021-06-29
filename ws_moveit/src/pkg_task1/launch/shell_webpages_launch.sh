#!/bin/bash

# Store URL in a variable
URL1="http://www.hivemq.com/demos/websocket-client/"
URL2="https://docs.google.com/spreadsheets/d/126KwTFJOQONOdse8_nd7q2dPtSV-RRaXWqOft_brqz8/edit?usp=sharing" 
# Print some message
echo "** Opening $URL1 in Firefox **"

# Use firefox to open the URL in new windows 
echo "** Opening $URL2 in Firefox **"
firefox -new-window $URL1 $URL2
