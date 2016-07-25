#
# infinite_recursion.py
#
import sys
print sys.getrecursionlimit()
sys.setrecursionlimit(50)
print sys.getrecursionlimit()
def recursion_depth(number):
    print "Recursion depth number %d." % number
    try:
        recursion_depth(number + 1)
    except:
        print "Maximum recursion depth exceeded."

recursion_depth(0)