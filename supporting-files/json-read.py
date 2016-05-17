__author__ = 'PRAYAS2'
import json
from pprint import pprint

data_file = open('sarcasm.json')
datawe = json.load(data_file)
l= datawe["d"]
for x in l :
    print(x["text"])
