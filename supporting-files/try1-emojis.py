import re
import codecs
import csv
f = codecs.open('NS-final.txt', encoding='utf-8')
count=[]
t=[]
laughexp=[]
for l in f:
    t.append(l)
    count.append(len(re.findall('[\U0001f600-\U0001f650]', l)))
    pat1=re.compile(r'(\blols?z?o?\b)+?',re.I)
    pat2=re.compile(r'(\brofl\b)+?',re.I)
    pat3=re.compile(r'(\blmao\b)+?',re.I)
    laughexp.append(len(re.findall(pat1,l)) + len(re.findall(pat2,l)) + len(re.findall(pat3,l)))
    try:
        next(f)
    except:
        break


print(len(t))   #list of text of tweet
print(count)  #count is list of number of emojis in tweet
print(laughexp)   #list of count of laughter expression in tweet : lol , rofl , lmao

with open('NON_Sarcastic_emoji_lol.csv','w',newline='') as csvfile:
    x=csv.writer(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
    x.writerow(['emoji_count','laughter_exp_count'])
    for i in range(len(t)):
        x.writerow([count[i],laughexp[i]])

