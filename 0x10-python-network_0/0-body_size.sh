#!/bin/bash
# Takes in a URL, sends a request to that URL, and displays the size of the body of the response
grep "Content-Length" <(curl -sI "$1") | cut -d " " -f2
