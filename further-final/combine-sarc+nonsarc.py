import csv
from random import shuffle
l=[]
with open('sarcstic-2353-labeled.csv') as csvfile:
    sreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in sreader:
        l.append(row)

with open('non-sarcastic-final-2738-labeled.csv') as csvfile:
    nsreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    count=0
    for row in nsreader:
        if count>0:
            l.append(row)
        count+=1

l1=l[1:]
for i in range(len(l1)):
    l1[i]=list(map(int,l1[i]))
shuffle(l1)
l=[l[0]]
l.extend(l1)
with open('data1.csv','w',newline='') as csvfile:
    x=csv.writer(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
    for row in l:
        x.writerow(row)


