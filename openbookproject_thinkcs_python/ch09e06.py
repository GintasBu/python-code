#  Add your doctests here:
"""
  >>> 13 in junk
  True
  >>> del junk[4]
  >>> junk
  [3, 7, 9, 10, 17, 21, 24, 27]
  >>> del junk[a:b]
  >>> junk
  [3, 7, 27]
  >>> import string
  >>> string.split(message, '??')
  ['this', 'and', 'that']
  
  
  
"""
junk=[3,7,9,10,13, 17,21,24,27]
a=2
b=len(junk)-2

nlist=[[0,0,17],[0,5,0],[0,0,0]]
# Write your Python code here:

message='this??and??that'

if __name__ == '__main__':
    import doctest
    doctest.testmod()