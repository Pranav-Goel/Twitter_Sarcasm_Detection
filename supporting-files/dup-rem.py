__author__ = 'PRAYAS2'
import json,os,re
cnt=0
tcnt=0
s=set()
with open("pranav-sarc-new.json") as f:
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
        try:
            if(jfile["text"][0:2]=="RT"):
                jfile["text"]=jfile["text"][3:]
            s.add(jfile["text"])
        except:
            break
f= open("pranav-sarcastic.txt","w")
for x in s :
    f.write(x.encode("utf-8"))
    f.write(os.linesep)