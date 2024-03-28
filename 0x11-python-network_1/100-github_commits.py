#!/usr/bin/python3
"""10. Time for an interview!"""
import sys
import requests

if __name__ == "__main__":
    repository_name = sys.argv[1]
    owner_name = sys.argv[2]
    
    response = requests.get(
            'https://developer.github.com/v3/repos/commits/', auth=(repository_name, owner_name))
    commits = response.json()

    try:
        for i in range(10):
            print("{}: {}".format(
                commits[i].get("sha"),
                commits[i].get("commit").get("author").get("name")))
    except IndexError:
        pass
