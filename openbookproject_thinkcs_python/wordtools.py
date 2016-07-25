def cleanword(word):
    """
      >>> cleanword('what?')
      'what'
      >>> cleanword('"now!"')
      'now'
      >>> cleanword('?+="word!,@$()"')
      'word'
    """
    import string
    l2=[]
    l=list(word)
    for i in range(len(l)):
        if l[i] in string.ascii_letters:
            l2.append(l[i])
    l3=''.join(l2)
    return l3

def has_dashdash(s):
    """
      >>> has_dashdash('distance--but')
      True
      >>> has_dashdash('several')
      False
      >>> has_dashdash('critters')
      False
      >>> has_dashdash('spoke--fancy')
      True
      >>> has_dashdash('yo-yo')
      False
    """
    
   # import string
    return '--' in s

def extract_words(s):
    """
      >>> extract_words('Now is the time!  "Now", is the time? Yes, now.')
      ['now', 'is', 'the', 'time', 'now', 'is', 'the', 'time', 'yes', 'now']
      >>> extract_words('she tried to curtsey as she spoke--fancy')
      ['she', 'tried', 'to', 'curtsey', 'as', 'she', 'spoke', 'fancy']
    """
    import string
    s=string.replace(s, '--', ' ')
    l=string.split(s)
    l2=[]
    
    for i in range(len(l)):
        l[i]=l[i].lower()
        l2.append(cleanword(l[i]))
    return l2

def wordcount(word, wordlist):
    """
      >>> wordcount('now', ['now', 'is', 'time', 'is', 'now', 'is', 'is'])
      ['now', 2]
      >>> wordcount('is', ['now', 'is', 'time', 'is', 'now', 'is', 'the', 'is'])
      ['is', 4]
      >>> wordcount('time', ['now', 'is', 'time', 'is', 'now', 'is', 'is'])
      ['time', 1]
      >>> wordcount('frog', ['now', 'is', 'time', 'is', 'now', 'is', 'is'])
      ['frog', 0]
    """
    import string
    x=wordlist.count(word)
    return [word, x]

def wordset(wordlist):
    """
      >>> wordset(['now', 'is', 'time', 'is', 'now', 'is', 'is'])
      ['is', 'now', 'time']
      >>> wordset(['I', 'a', 'a', 'is', 'a', 'is', 'I', 'am'])
      ['I', 'a', 'am', 'is']
      >>> wordset(['or', 'a', 'am', 'is', 'are', 'be', 'but', 'am'])
      ['a', 'am', 'are', 'be', 'but', 'is', 'or']
    """
    ll=[]
    while len(wordlist)>0:
        l=wordlist[0]
        while l in wordlist: wordlist.remove(l)
        ll.append(l)
    ll.sort()
    return ll

def longestword(wordset):
    """
      >>> longestword(['a', 'apple', 'pear', 'grape'])
      5
      >>> longestword(['a', 'am', 'I', 'be'])
      2
      >>> longestword(['this', 'that', 'supercalifragilisticexpialidocious'])
      34
    """    
    le=0
    for i in range(len(wordset)):
        if len(wordset[i])>le:
            le=len(wordset[i])
    return le
    
if __name__ == '__main__':
    import doctest
    doctest.testmod()