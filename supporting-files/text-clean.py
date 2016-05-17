__author__ = 'PRAYAS2'
f = open('non-sarc-edu.txt')
f2 = open('non-sarc-edu2.txt',mode='w')

cnt=0
for l in f :
    next(f)
    f2.write(l)

print(cnt)