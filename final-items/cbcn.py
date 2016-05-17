__author__ = 'PRAYAS2'
import re
import codecs
f = codecs.open('Unique-tweets-sarc-comb2.txt20160311-215402 - Copy.txt', encoding='utf-8')
count=[]
t=[]
for l in f:
    t.append(l)
    count.append(len(re.findall('[\U0001f600-\U0001f650]', l)))
    try:
        next(f)
    except:
        break

print(t)
print(count)