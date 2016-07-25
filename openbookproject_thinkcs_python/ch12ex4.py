import string

alice_file=open('alice_in_wonderland.txt', 'r')

dict={}


for line in alice_file:
    line=line.translate(None, string.punctuation)
    #line=line.lower()
    line.rsplit()
    words=line.split()
    for word in words:
        word=word.lower()
        #print type(word)
        dict[word]=dict.get(word, 0)+1
    #return dict

dict2=sorted(dict.items(), key=lambda x:x[0])
wl=''
l=0
for it in dict2:
    if len(it[0])>len(wl):
        wl=it[0]
        l=len(it[0])
     #print it

alice_file.close()
print wl, l

#word alice was 386 times. alices 12