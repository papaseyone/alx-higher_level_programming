#!/bin/bash
# it taske URL, Display all HTTP methods the server will accept.
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
