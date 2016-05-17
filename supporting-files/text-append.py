__author__ = 'PRAYAS2'
import os
cnt=0
import codecs
f1 = codecs.open('pranav-sarcastic-dup-rem.txt', encoding='utf-8')

f2 = codecs.open('Unique-tweets-sarc-comb2.txt20160311-215402 - Copy.txt', encoding='utf-8')
f3= codecs.open('pranav+old.txt', encoding='utf-8',mode='w')
s=set()
for l in f1 :
    s.add(l)
for l in f2 :
    s.add(l)

for x in s :
    f3.write(x)
    cnt=cnt+1
    #f3.write(os.linesep)
print(cnt)
