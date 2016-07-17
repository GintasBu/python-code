import sys
import json
import re
str_data = open(sys.argv[1])
counts=dict()
wordlist=list()
for entry in str_data:
    json_data=json.loads(entry)
    try: text=json_data["text"]
    except: text=''
    text=text.strip('\n')
    text=text.strip('\t')
    text = text.replace('\n','')
    text = text.replace('\t','')
    text = re.sub(ur'[^\w\d\s]+', '', text)
    words=text.split(' ')
    for word in words:
        if len(word)>0:
            word=word.encode('utf-8')
            if word not in counts:
                counts[word] = 1
            else:
                counts[word] += 1
    
S=sum(counts.values())
for i in range(len(counts.keys())):
    ww=counts.keys()[i]
    a=counts.values()[i]
    print ww, round(float(counts.values()[i])/S, 4)
