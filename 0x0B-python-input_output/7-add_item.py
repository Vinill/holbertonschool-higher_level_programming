#!/usr/bin/python3
"""
function that creates an Object from a “JSON file”
"""
import sys


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
file_name = "add_item.json"
obj = [arg for arg in sys.argv if arg != sys.argv[0]]

try:
    file_7 = load_from_json_file(file_name)
except FileNotFoundError:
    save_to_json_file(obj, file_name)
else:
    for i in obj:
        file_7.append(i)
    save_to_json_file(file_7, file_name)
