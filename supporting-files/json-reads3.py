__author__ = 'PRAYAS2'
import json,os,re
cnt=0
tcnt=0
with open("Abcd.json") as f:
    for line in f:
        while True:
            try:
                jfile = json.loads(line)
                break
            except ValueError:
                # Not yet a complete JSON value
                line += next(f)
        #if(jfile["in_reply_to_status_id"]!=None):
         #   cnt=cnt+1
        print(jfile["text"])