__author__ = 'PRAYAS2'
__author__ = 'PRAYAS2'
import json,os,re
cnt=0
tcnt=0
pat = re.compile('\#happy|\#sad|\#joy|\#happiness',re.I)

pat3= re.compile('http[^\s,]+')
pat4 = re.compile('@[^\s,]+')
pat5 = re.compile('(:\))|(\;\))|(:D)|(:P)')
pat6 = re.compile('([?!,\.&])')
pat7=re.compile(re.escape('\n'))
pat8=re.compile('[\s]+')
tfile=open("non-sarcastic-c.json","a")
with open("non-sarcastic.json") as f:
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
        tcnt=tcnt+1
        ttext=jfile["text"]
        del jfile["text"]
        ttext=pat.sub('',ttext)
        #ttext=pat2.sub('',ttext)
        ttext = pat3.sub('HYPERLINK',ttext)
        ttext = pat4.sub('NAME',ttext)
        #ttext = pat5.sub('EMOTICON',ttext)
        ttext = pat6.sub(r' \1 ',ttext)
        ttext=pat7.sub('',ttext)
        ttext=pat8.sub(' ',ttext)
        print(ttext)
        jfile["text"]=ttext
        json.dump(jfile,tfile)
        tfile.write(os.linesep)
        #if(tcnt%100==0):
        print((tcnt))
