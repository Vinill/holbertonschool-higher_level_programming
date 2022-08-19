#!/usr/bin/python3
"""Python script that takes in a URL, sends a request to the URL and
displays the body of the response"""

if __name__ == "__main__":
    import requests
    from sys import argv

    url = argv[1]
    req = requests.get(url)

    if req:
        print(req.text)
    else:
        print("Error code:", req.status_code)
