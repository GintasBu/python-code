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


for it in dict2[:150]:

     print it

alice_file.close()


#word alice was 386 times. alices 12