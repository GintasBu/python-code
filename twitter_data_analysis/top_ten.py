import sys
import json
str_data = open(sys.argv[1])
words=dict()
for entry in str_data:
    count=0
    json_data=json.loads(entry)
    try:
        place=json_data["entities"]["hashtags"]
    except:
        place='nera'
    #print place        
    if place!="nera":
        if len(place)>0:
            place=place[0]
            txt=place['text']
            txt=txt.encode('utf-8')
            words[txt] = words.get(txt,0) + 1   
lst = list()
for key, val in words.items():
    lst.append( (val, key) )
lst.sort(reverse=True)
for key, val in lst[:10] :
    print val, key
