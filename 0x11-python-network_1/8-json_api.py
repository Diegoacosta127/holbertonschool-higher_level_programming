#!/usr/bin/python3
"""
Python script that takes in a letter and sends a POST request to a url with
the letter as a parameter
Letter is sent in the variable q 
If no argument is given, sets q=""
If the response body is properly JSON formatted and not empty, displays the
id and name like this: [<id>] <name>
Otherwise:
- Display 'Not a valid JSON' if the JSON is invalid
- Display 'No result' if the JSON is empty
"""
import requests
from sys import argv


if __name__ == "__main__":
    if len(argv) > 1:
        datum = {'q': argv[1]}
    else:
        datum = {'q': ""}

    r = requests.post('http://0.0.0.0:5000/search_user', data=datum)

    try:
        req = r.json()
        if len(req) == 0:
            print("No result")
        else:
            print("[{}] {}".format(req.get('id'), req.get('name')))
    except:
        print("Not a valid JSON")
