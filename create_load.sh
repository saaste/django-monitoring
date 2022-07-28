#!/bin/bash
set -B
while true
do
    curl -s -k 'GET' 'http://localhost:8000/dogs/' > /dev/null
    echo "Request sent"
    sleep 1
done