import sys

x=sys.argv[1]
n=1
f=1
y=int(x)
if y==0: 
    print n
else: 
    while n<=y:
        f=n*f
        n=n+1
    print f