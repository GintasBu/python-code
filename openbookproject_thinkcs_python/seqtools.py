def encapsulate(val, seq):
    """
   
    """
    if type(seq) == type(""):
        return str(val)
    if type(seq) == type([]):
        return [val]
    return (val,)
    
def insert_in_middle(val, seq):
    """
    >>> insert_in_middle('c', ['a', 'b', 'd', 'e'])
    ['a', 'b', 'c', 'd', 'e']
    >>> insert_in_middle('c', ('a', 'b', 'd', 'e'))
    ('a', 'b', 'c', 'd', 'e')
    """
    middle = len(seq)/2
    return seq[:middle] + encapsulate(val, seq) + seq[middle:]
    

def make_empty(seq):
    """
      >>> make_empty([1, 2, 3, 4])
      []
      >>> make_empty(('a', 'b', 'c'))
      ()
      >>> make_empty("No, not me!")
      ''
    """
    if type(seq)==type(""):
        return ''
    if type(seq)==type([]):
        return []
    if type(seq)==type(()):
        return ()
    

    
def insert_at_end(val, seq):
    """
      >>> insert_at_end(5, [1, 3, 4, 6])
      [1, 3, 4, 6, 5]
      >>> insert_at_end('x', 'abc')
      'abcx'
      >>> insert_at_end(5, (1, 3, 4, 6))
      (1, 3, 4, 6, 5)
    """
    return seq+encapsulate(val, seq)

def insert_in_front(val, seq):
    """
      >>> insert_in_front(5, [1, 3, 4, 6])
      [5, 1, 3, 4, 6]
      >>> insert_in_front(5, (1, 3, 4, 6))
      (5, 1, 3, 4, 6)
      >>> insert_in_front('x', 'abc')
      'xabc'
    """
    return encapsulate(val, seq)+seq
    

def index_of(val, seq, start=0):
    """
      >>> index_of(9, [1, 7, 11, 9, 10])
      3
      >>> index_of(5, (1, 2, 4, 5, 6, 10, 5, 5))
      3
      >>> index_of(5, (1, 2, 4, 5, 6, 10, 5, 5), 4)
      6
      >>> index_of('y', 'happy birthday')
      4
      >>> index_of('banana', ['apple', 'banana', 'cherry', 'date'])
      1
      >>> index_of(5, [2, 3, 4])
      -1
      >>> index_of('b', ['apple', 'banana', 'cherry', 'date'])
      -1
    """
    import string
    if type(seq)==type(""):
        seq2=seq[start:]
        i=seq2.find(val)
        return i+start 
        
    if type(seq)==type([]):
        l2=seq[start:]
        try: i=l2.index(val)
        except: i=-1
        return i+start

    if type(seq)==type(()):
        l2=seq[start:]
        i=l2.index(val)
        return i+start        
 
def remove_at(index, seq):
    """
      >>> remove_at(3, [1, 7, 11, 9, 10])
      [1, 7, 11, 10]
      >>> remove_at(5, (1, 4, 6, 7, 0, 9, 3, 5))
      (1, 4, 6, 7, 0, 3, 5)
      >>> remove_at(2, "Yomrktown")
      'Yorktown'
    """
    import string
    if type(seq)==type(""):
        return seq[:index]+seq[index+1:] 
        
    if type(seq)==type([]):
        seq.pop(index)
        return seq

    if type(seq)==type(()):
        return seq[:index]+seq[index+1:]     

def remove_all(val, seq):
    """
      >>> remove_all(11, [1, 7, 11, 9, 11, 10, 2, 11])
      [1, 7, 9, 10, 2]
      >>> remove_all('i', 'Mississippi')
      'Msssspp'
    """
    
    import string
    if type(seq)==type(""):
        while val in seq:
            i=seq.find(val)
            seq=seq[:i]+seq[i+1:]
        return seq
        
    if type(seq)==type([]):
        while val in seq:   
            seq.remove(val)
        return seq
        
 
def count(val, seq):
    """
      >>> count(5, (1, 5, 3, 7, 5, 8, 5))
      3
      >>> count('s', 'Mississippi')
      4
      >>> count((1, 2), [1, 5, (1, 2), 7, (1, 2), 8, 5])
      2
    """
    import string
    c=0
    if type(seq)==type(""):
        while val in seq:
            c+=1
            i=seq.find(val)
            seq=seq[:i]+seq[i+1:]
        return c 
        
    if type(seq)==type([]):
        c=seq.count(val)
        return c

    if type(seq)==type(()):
        while val in seq:
            c+=1
            i=seq.index(val)
            seq=seq[:i]+seq[i+1:]
        return  c   

def reverse(seq):
    """
      >>> reverse([1, 2, 3, 4, 5])
      [5, 4, 3, 2, 1]
      >>> reverse(('shoe', 'my', 'buckle', 2, 1))
      (1, 2, 'buckle', 'my', 'shoe')
      >>> reverse('Python')
      'nohtyP'
    """

    import string
       
    if type(seq)==type(""):
        s=list(seq)
        s.reverse()
        s=''.join(s)
        return s  
        
    if type(seq)==type([]):
        seq.reverse()
        return seq

    if type(seq)==type(()):
        s=list(seq)
        s.reverse()
        c=tuple(s)
        return  c   

def sort_sequence(seq):
    """
      >>> sort_sequence([3, 4, 6, 7, 8, 2])
      [2, 3, 4, 6, 7, 8]
      >>> sort_sequence((3, 4, 6, 7, 8, 2))
      (2, 3, 4, 6, 7, 8)
      >>> sort_sequence("nothappy")
      'ahnoppty'
    """ 
    import string
       
    if type(seq)==type(""):
        s=list(seq)
        s.sort()
        s=''.join(s)
        return s  
        
    if type(seq)==type([]):
        seq.sort()
        return seq

    if type(seq)==type(()):
        s=list(seq)
        s.sort()
        c=tuple(s)
        return  c   


 
if __name__=='__main__':
    import doctest
    doctest.testmod()