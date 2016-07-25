def replace(s, old, new):
    """
      >>> replace('Mississippi', 'i', 'I')
      'MIssIssIppI'
      >>> s = 'I love spom!  Spom is my favorite food.  Spom, spom, spom, yum!'
      >>> replace(s, 'om', 'am')
      'I love spam!  Spam is my favorite food.  Spam, spam, spam, yum!'
      >>> replace(s, 'o', 'a')
      'I lave spam!  Spam is my favarite faad.  Spam, spam, spam, yum!'
    """
    import string
    ss=''
    s2=[]
    j=0
    #for t in string.split(s):
    t=[s]    
    while j>-1:
        j=string.find(t[0], old, j)
        if j!=-1:
            ss=t[0][:j]+new+t[0][j+len(old):]
            t[0]=ss
    s2.append(ss)
    return string.join(s2)
    
    
    
    
    
if __name__ == '__main__':
    import doctest
    doctest.testmod()