def reverse(s):
    """
      >>> reverse('happy')
      'yppah'
      >>> reverse('Python')
      'nohtyP'
      >>> reverse("")
      ''
      >>> reverse("P")
      'P'
    """
    i=len(s)-1
    ss=""
    while i>=0:
        ch=s[i]
        ss=ss+ch
        i-=1
    return ss
    
    
def mirror(s):
    """
      >>> mirror("good")
      'gooddoog'
      >>> mirror("yes")
      'yessey'
      >>> mirror('Python')
      'PythonnohtyP'
      >>> mirror("")
      ''
      >>> mirror("a")
      'aa'
    """    
    return s+reverse(s)
    

def remove_letter(letter, strng):
    """
      >>> remove_letter('a', 'apple')
      'pple'
      >>> remove_letter('a', 'banana')
      'bnn'
      >>> remove_letter('z', 'banana')
      'banana'
      >>> remove_letter('i', 'Mississippi')
      'Msssspp'
    """
    s=''
    for char in strng:
        if char != letter:
            s=s+char
    return s

    
def is_palindrome(s):
    """
      >>> is_palindrome('abba')
      True
      >>> is_palindrome('abab')
      False
      >>> is_palindrome('tenet')
      True
      >>> is_palindrome('banana')
      False
      >>> is_palindrome('straw warts')
      True
    """    
    return s==reverse(s)
    
    
def count(sub, s):
    """
      >>> count('is', 'Mississippi')
      2
      >>> count('an', 'banana')
      2
      >>> count('ana', 'banana')
      2
      >>> count('nana', 'banana')
      1
      >>> count('nanan', 'banana')
      0
    """
    import string
    i=0
    count=0
    while i<len(s):
        j=string.find(s, sub, i)
        if j==-1:
            i=i+1
        else: 
            i=j+1
            count+=1
    return count
    
    
def remove(sub, s):
    """
      >>> remove('an', 'banana')
      'bana'
      >>> remove('cyc', 'bicycle')
      'bile'
      >>> remove('iss', 'Mississippi')
      'Missippi'
      >>> remove('egg', 'bicycle')
      'bicycle'
    """
    import string
    j=string.find(s, sub)
    if j==-1:
        return s
    else: 
        s2=s[:j]+s[j+len(sub):]
    return s2
  

def remove_all(sub, s):
    """
      >>> remove_all('an', 'banana')
      'ba'
      >>> remove_all('cyc', 'bicycle')
      'bile'
      >>> remove_all('iss', 'Mississippi')
      'Mippi'
      >>> remove_all('eggs', 'bicycle')
      'bicycle'
    """
    j=0
    import string
    while j>-1:
        j=string.find(s, sub)
        if j==-1:
            return s
        else: 
            s2=s[:j]+s[j+len(sub):]
            s=s2
    return s

  
if __name__ == '__main__':
    import doctest
    doctest.testmod()