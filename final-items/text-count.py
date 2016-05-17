__author__ = 'PRAYAS2'
cnt=0
f = open('appended.txt')

for l in f :
    cnt=cnt+1
    next(f)
    #print(l[:-1])

print(cnt)
