import codecs
from random import shuffle
f1 = codecs.open('sarc-libsvm.txt', encoding='utf-8')
f2 = codecs.open('ns-lib2.txt', encoding='utf-8')
f3 = open('libsvm_data2.txt','w')
l=[]
for line in f1:
    l.append(line[:-3])

for lin in f2:
    l.append(lin[:-3])

shuffle(l)
print(l)
for s in l:
    f3.write(s+'\n')