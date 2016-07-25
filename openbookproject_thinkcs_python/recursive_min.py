def recursive_min(nested_num_list):
    """
      >>> recursive_min([2, 9, [1, 13], 8, 6])
      1
      >>> recursive_min([2, [[100, 1], 90], [10, 13], 8, 6])
      1
      >>> recursive_min([2, [[13, -7], 90], [1, 100], 8, 6])
      -7
      >>> recursive_min([[[-13, 7], 90], 2, [-51, 100], 8, 6])
      -51
    """
    smallest = nested_num_list[0]
    while type(smallest) == type([]):
        smallest = smallest[0]

    for element in nested_num_list:
        if type(element) == type([]):
            min_of_elem = recursive_min(element)
            if smallest > min_of_elem:
                smallest = min_of_elem
        else:                           # element is not a list
            if smallest > element:
                smallest = element

    return smallest    
    
    
if __name__=='__main__':
    import doctest
    doctest.testmod()