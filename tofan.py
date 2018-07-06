import json
from pprint import pprint

with open('impressions-shortlist', 'r') as f:
    for line in f:
        data = json.loads(line)
        pprint(data)


