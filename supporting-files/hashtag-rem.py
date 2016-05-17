

__author__ = 'PRAYAS2'
import re,os,time
pat= re.compile('#')
f=open('pranav+old.txt')
f2=open('pranav+old+final.txt',mode='w')

for l in f :
    #k=re.sub(pat,'',l)
    k=l.replace('#','')
    print(l)
    f2.write(k)