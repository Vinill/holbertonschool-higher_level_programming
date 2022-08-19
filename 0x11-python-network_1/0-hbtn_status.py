#!/usr/bin/python3
"""Python script that fetches https://intranet.hbtn.io/status"""
if __name__ == "__main__":
    from urllib import request
    with request.urlopen('https://intranet.hbtn.io/status') as response:
        content_body = response.read()
        print("Body response:")
        print("\t- type:", type(content_body))
        print("\t- content:", content_body)
        print("\t- utf8 content:", content_body.decode("utf-8"))
