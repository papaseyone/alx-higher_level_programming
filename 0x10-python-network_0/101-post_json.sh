#!/bin/bash
# Sends JSON POST request to URL and displays the body response.
curl -s -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
