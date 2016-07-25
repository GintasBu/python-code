def only_evens(numbers):
    """
      >>> only_evens([1, 3, 4, 6, 7, 8])
      [4, 6, 8]
      >>> only_evens([2, 4, 6, 8, 10, 11, 0])
      [2, 4, 6, 8, 10, 0]
      >>> only_evens([1, 3, 5, 7, 9, 11])
      []
      >>> only_evens([4, 0, -1, 2, 6, 7, -4])
      [4, 0, 2, 6, -4]
      >>> nums = [1, 2, 3, 4]
      >>> only_evens(nums)
      [2, 4]
      >>> nums
      [1, 2, 3, 4]
    """
    l=[]
    for n in numbers:
        if n%2==0:
            l.append(n)
    return l
    
def only_odds(numbers):
    """
      >>> only_odds([1, 3, 4, 6, 7, 8])
      [1, 3, 7]
      >>> only_odds([2, 4, 6, 8, 10, 11, 0])
      [11]
      >>> only_odds([1, 3, 5, 7, 9, 11])
      [1, 3, 5, 7, 9, 11]
      >>> only_odds([4, 0, -1, 2, 6, 7, -4])
      [-1, 7]
      >>> nums = [1, 2, 3, 4]
      >>> only_odds(nums)
      [1, 3]
      >>> nums
      [1, 2, 3, 4]
    """
    l=[]
    for n in numbers:
        if n%2!=0:
            l.append(n)
    return l

def multiples_of(num, numlist):
    """
      >>> multiples_of(4, [1, 3, 4, 6, 7, 8])
      [4, 8]
      >>> multiples_of(11, [2, 4, 6, 8, 10, 11, 0])
      [11]
      >>> multiples_of(7, [1, 3, 5, 7, 9, 11])
      [7]
      >>> nums = [1, 2, 3, 4]
      >>> multiples_of(2, nums)
      [2, 4]
      >>> nums
      [1, 2, 3, 4]
    """
    l=[]
    for n in numlist:
        if n%num==0 and n!=0:
            l.append(n)
    return l
    
    
if __name__ == '__main__':
    import doctest
    doctest.testmod()