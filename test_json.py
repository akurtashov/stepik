import json
import sys

data = [
        {'name': 'AA' 'parents': []},
        {'name': 'BB', 'parents': ['AA', 'CC']            },
        {'name': 'CC', 'parents': ['AA']},
        {'name': 'DD', 'parents': ['CC']},
        {'name': 'EE', 'parents': ['DD']},
        {'name': 'FF', 'parents': ['DD']},
        {'name': 'GG', 'parents': ['EE']},
        ]

with open('test2.json', 'w') as json_file:
    json.dump(data, json_file, indent = 4, sort_keys= True)


data_in = []
with open('test.json') as json_file:
    data_in = json.load(json_file)

#data_in = json.load(sys.stdin)

print(data_in)
