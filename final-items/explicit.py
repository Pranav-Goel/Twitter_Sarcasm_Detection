__author__ = 'PRAYAS2'
import re,os
pat = re.compile(r'.*[\t][0-9][\t]\-[0-9][\t](.*)')
pat2=re.compile(r'\[\[.*?\]\]')
f = open('pranav+old+results.txt')
f2 = open('pranav+old+results-clean.txt',mode='w')
for x in f:
    l=pat.findall(x)[0]
    l=re.sub(pat2,'',l)
    l=l[:-2]
    f2.write(l)
    f2.write(os.linesep)