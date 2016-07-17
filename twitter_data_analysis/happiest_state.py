import sys
import json
import re

states = {
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AS': 'American Samoa',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DC': 'District of Columbia',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'GU': 'Guam',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MP': 'Northern Mariana Islands',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NA': 'National',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'PR': 'Puerto Rico',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VI': 'Virgin Islands',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming'
}
state=states.keys()
afinnfile = open(sys.argv[1])
scores = {} # initialize an empty dictionary
stl=[]
stlc=[]
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
    if bool(text)==1:
        text=text.strip('\n')
        text=text.strip('\t')
        text = text.replace('\n','')
        text = text.replace('\t','')
        text=text.encode('utf-8')
        text = re.sub(ur'[^\w\d\s]+', '', text)
        words=text.split(' ')
        for w in words:
            if w in scores:
                count=count+scores[w]
            else: 
                count=count+0
        #print count
        try:
            place=json_data["place"]["full_name"]
        except:
            place='nera'
            
        if place!="nera":
            text=place.strip('\n')
            text=text.strip('\t')
            text = text.replace('\n','')
            text = text.replace('\t','')
            place=text.encode('utf-8')
            #text = re.sub(ur'[^\w\d\s]+', '', text)
            #print place
            if len(place.split(', '))>1:
                st=place.split(', ')[1]
                if st in state:
                    #print st, count
                    stl.append(st)
                    stlc.append(count)
#print stlc.index(max(stlc))      
#print stlc, stlc[stlc.index(max(stlc))]
print stl[stlc.index(max(stlc))]