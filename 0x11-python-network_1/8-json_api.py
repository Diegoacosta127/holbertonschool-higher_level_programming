#!/usr/bin/python3
"""
Python script that takes in a letter and sends a POST request to a url with
the letter as a parameter
* Letter is sent in the variable q 
* If no argument is given, sets q=""
* If the response body is properly JSON formatted and not empty, displays the
id and name like this: [<id>] <name>
* Otherwise:
    Display 'Not a valid JSON' if the JSON is invalid
    Display 'No result' if the JSON is empty
"""
import requests
from sys import argv


if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    if len(argv) > 1:
        q = argv[1]
    else:
        q = ""
    r = requests.post(url, data={"q": q})
    try:
        if r.json():
            print("[{}] {}".format(r.json()["id"], r.json()["name"]))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
