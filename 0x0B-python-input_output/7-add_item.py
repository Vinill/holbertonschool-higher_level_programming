#!/usr/bin/python3
"""
function that creates an Object from a “JSON file”
"""

from sys import argv

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

file_name = "add_item.json"

try:
    file_7 = load_from_json_file(file_name)
except FileNotFoundError:
    file_7 = []

save_to_json_file(file_7 + argv[1:], file_name)
