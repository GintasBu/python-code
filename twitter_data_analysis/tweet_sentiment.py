import sys
import json
afinnfile = open(sys.argv[1])
scores = {} # initialize an empty dictionary
for line in afinnfile:
  term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
  scores[term] = int(score)  # Convert the score to an integer.
str_data = open(sys.argv[2])
for entry in str_data:
    count=0
    json_data=json.loads(entry)
    try:
        text=json_data["text"]
    except:
        text='0'
    words=text.split(' ')
    for w in words:
        if w in scores:
            count=count+scores[w]
        else: 
            count=count+0
    print count