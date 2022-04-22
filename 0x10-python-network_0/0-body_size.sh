#!/bin/bash
# This script is used to calculate the body size of a HTTP request.
curl -sI $1 | grep "Content-Length" | cut -d " " -f 2