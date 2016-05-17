f=open('pranav-sarcastic.txt',mode='r')
f2=open('pranav-sarcastic-dup-rem.txt',mode="w")
s=set()
cnt=0
for l in f :
    s.add(l)
for x in s :
    f2.write(x)
    cnt=cnt+1
print(cnt)