import json
import sys

data = [
        {'name': 'A', 'parents': []},
        {'name': 'B', 'parents': ['A', 'C']            },
        {'name': 'C', 'parents': ['A']},
        {'name': 'D', 'parents': ['C']},
        {'name': 'E', 'parents': ['D']},
        {'name': 'F', 'parents': ['D']},
        {'name': 'G', 'parents': ['E']},
        ]

with open('test2.json', 'w') as json_file:
    json.dump(data, json_file, indent = 4, sort_keys= True)


data_in = []
with open('test.json') as json_file:
    data_in = json.load(json_file)

#data_in = json.load(sys.stdin)

print(data_in)
