import re,csv
import codecs
from random import shuffle

f1 = codecs.open('pranav+old+final.txt', encoding='utf-8')
csvfile = open('sarcstic-2353.csv','r')
f2=codecs.open('vocab.txt', encoding='utf-8')
f3 = open('sarc-libsvm.txt','w')
vocab={}
f4=csv.reader(csvfile, delimiter=' ', quotechar='|')
for x in f2:
    x=x.rstrip('\n')
    id,word=x.split(':',1)
    vocab[word]=id
cnt=0
l10=[]
ind=0
for l1 in f4:
    l1=l1[0].split(',')
    l10.append(l1)

l10=l10[1:]
print(l10)
for l in f1:
    cnt=cnt+1
    words=l.split(' ')
    feature_dic ={}
    for word in words:
        try:

                id=vocab[word]
        except:
            continue
        try:
            feature_dic[id]=feature_dic[id]+1
        except:
            feature_dic[id]=1
    #print(feature_dic)
    for i in range(10):
        feature_dic[i+1]=int(l10[ind][i])

    feature_list=[]
    ind+=1
    for key in feature_dic.keys():
        feature_list.append((int(key),feature_dic[key]))
    feature_list.sort(key=lambda tup:tup[0])
    print(feature_list)
    f3.write('1 ')
    for x in feature_list:
        s=str(x[0])+':'+str(x[1])+' '
        f3.write(s)
    f3.write('\n')
    #try:
        #next(f1)
    #except:
        #pass
print(cnt)

