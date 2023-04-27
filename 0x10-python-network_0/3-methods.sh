#!/bin/bash
# Takes in a URL and displays all HTTP methods the server will accept.
grep "Allow:" <(curl -sI "$1") | cut -d " " -f2-
