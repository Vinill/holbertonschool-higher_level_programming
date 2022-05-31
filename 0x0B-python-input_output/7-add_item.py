#!/usr/bin/python3
"""
function that creates an Object from a “JSON file”
"""
import sys

if __name__ == "__main__":
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = \
        __import__('6-load_from_json_file').load_from_json_file

    try:
        file_7 = load_from_json_file('add_item.json')
    except FileNotFoundError:
        file_7 = []
    file_7.extend(sys.argv[1:])
    save_to_json_file(file_7, 'add_item.json')
