#!/usr/bin/python3
"""10. Time for an interview!"""
import sys
import requests

if __name__ == "__main__":
    repository_name = sys.argv[1]
    owner_name = sys.argv[2]

    url = "https://api.github.com/repos/{}/{}commits".format(
            owner_name, repository_name)
    response = requests.get(url)

    if response.status_code == 200:
        commits = response.json()

        for commit in commits[:10]:
            sha = commit['sha']
            author_name = commit['commit']['author']['name']
            print(f"{sha}: {author_name}")
    else:
        print(f"Error: {response.status_code}")
