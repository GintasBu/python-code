def add_vectors(u, v):
    """
      >>> add_vectors([1, 0], [1, 1])
      [2, 1]
      >>> add_vectors([1, 2], [1, 4])
      [2, 6]
      >>> add_vectors([1, 2, 1], [1, 4, 3])
      [2, 6, 4]
      >>> add_vectors([11, 0, -4, 5], [2, -4, 17, 0])
      [13, -4, 13, 5]
    """

# Write your Python code here:
    x=v[:]
    if len(u)==len(v):
        for i in range(len(u)):
            x[i]=u[i]+v[i]
        return x
    else:
        return 'u and v must be the same length'
        
def scalar_mult(s, v):
    """
    >>> scalar_mult(5, [1, 2])
    [5, 10]
    >>> scalar_mult(3, [1, 0, -1])
    [3, 0, -3]
    >>> scalar_mult(7, [3, 0, 5, 11, 2])
    [21, 0, 35, 77, 14]
    
    """   
    x=v[:]
    for i in range(len(v)):
            x[i]=s*v[i]
    return x    
        
def dot_product(u, v):
    """
      >>> dot_product([1, 1], [1, 1])
      2
      >>> dot_product([1, 2], [1, 4])
      9
      >>> dot_product([1, 2, 1], [1, 4, 3])
      12
      >>> dot_product([2, 0, -1, 1], [1, 5, 2, 0])
      0
    """        
    x=v[:]
    if len(u)==len(v):
        for i in range(len(u)):
            x[i]=u[i]*v[i]
        
    else:
        return 'u and v must be the same length'    
    return sum(x)    
        
        
if __name__ == '__main__':
    import doctest
    doctest.testmod()