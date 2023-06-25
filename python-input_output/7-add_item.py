#!/usr/bin/python3
"""
    This module contains a script that adds all arguments to a Python list
"""
import sys
import os


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

argument_list = []

path = 'add_item.json'
if os.path.isfile(path):
    argument_list = load_from_json_file("add_item.json")

args = sys.argv[1:]

for arg in args:
    argument_list.append(arg)

save_to_json_file(argument_list, "add_item.json")
