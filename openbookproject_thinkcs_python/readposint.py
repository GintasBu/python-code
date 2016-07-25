n=input("please enter a positive integer: ")
if n<=0:
    raise ValueError, '%s is not a positive integer' % n

if type(n)==type(3.145):
    raise ValueError, '%f is not an integer' % n 