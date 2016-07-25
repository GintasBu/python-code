import sys

filename=sys.argv[1]

file=open(filename,'r')
tt=[]
t=file.readlines()
t.sort()
#print t

outfile=open('sorted_fruit.txt', 'w')
for l in t: outfile.write(l)
outfile.close()
file.close()