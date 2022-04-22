#!/bin/bash
# This script is used to calculate the body size of a HTTP request.
curl -sI 0.0.0.0:5000 | grep "Content-Length" | cut -d " " -f 2