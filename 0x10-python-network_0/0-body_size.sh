#!/bin/bash
# Get the size of the response body in bytes from a given URL.
curl -sI "$1" | wc -c
