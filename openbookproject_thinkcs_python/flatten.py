def flatten(nested_num_list):
    """
      >>> flatten([2, [[[9]]], [2, [1, 13], 2], 8, [2, 6]])
      [2, 9, 2, 1, 13, 2, 8, 2, 6]
      >>> flatten([[9, [7, 1, 13, 2], 8], [7, 6]])
      [9, 7, 1, 13, 2, 8, 7, 6]
      >>> flatten([[9, [7, 1, 13, 2], 8], [2, 6]])
      [9, 7, 1, 13, 2, 8, 2, 6]
      >>> flatten([[5, [5, [1, 5], 5], 5], [5, 6]])
      [5, 5, 1, 5, 5, 5, 5, 6]
    """
    lst=[]

    for element in nested_num_list:
        if type(element) == type([]):
            element = flatten(element)
            for el in element:
                lst.append(el)
        else:    
            lst.append(element)     # element is not a list
            

    return lst
    
    
if __name__=='__main__':
    import doctest
    doctest.testmod()
    
