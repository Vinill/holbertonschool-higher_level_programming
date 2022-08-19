#!/usr/bin/python3
"""Python script that takes your GitHub credentials (username and password) and uses the GitHub API to display your id"""

if __name__ == "__main__":
    import requests
    from sys import argv

    user = argv[1]
    token = argv[2]

    res = requests.get('https://api.github.com/user', auth=(user, token))
    json = res.json()
    try:
        print(res.json()['id'])
    except Exception:
        print(None)
