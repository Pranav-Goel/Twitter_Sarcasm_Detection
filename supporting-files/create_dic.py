import codecs
import re
f1=codecs.open('pranav+old+final.txt', encoding='utf-8')
f2=codecs.open('NS-final.txt', encoding='utf-8')

s=set()
for x in f1:
    pat=r'[\U0001f600-\U0001f650]'
    re.sub(pat,'',x)
    l=x.split()
    for word in l:
        word=word.lower()
        s.add(word)

for x in f2:
    pat=r'[\U0001f600-\U0001f650]'
    re.sub(pat,'',x)
    l=x.split()
    for word in l:
        word=word.lower()
        s.add(word)
print(s)
print(len(s))

dic={}
i=11
for q in s:
    dic[i]= q
    i+=1


f3=codecs.open('vocab.txt','w',encoding='utf-8')
for x in dic:
    f3.write(str(x)+':'+dic[x]+'\n')