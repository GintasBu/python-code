def recursive_count(target, nested_num_list):
    """
      >>> recursive_count(2, [2, 9, [2, 1, 13, 2], 8, [2, 6]])
      4
      >>> recursive_count(7, [[9, [7, 1, 13, 2], 8], [7, 6]])
      2
      >>> recursive_count(15, [[9, [7, 1, 13, 2], 8], [2, 6]])
      0
      >>> recursive_count(5, [[5, [5, [1, 5], 5], 5], [5, 6]])
      6
    """
   
    c=0
    for element in nested_num_list:
        if type(element) == type([]):
            rec_of_elem = recursive_count(target, element)
            c+=rec_of_elem
        else:                           # element is not a list
            if target == element:
                c+=1
    return c    
 
if __name__=='__main__':
    import doctest
    doctest.testmod()