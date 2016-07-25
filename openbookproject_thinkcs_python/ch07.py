prefixes = "JKLMNOPQ"
suffix = "ack"
suffix2="uack"
for letter in prefixes:
    if letter=='O' or letter=='Q':
        print letter + suffix2
    else:
        print letter+suffix
        
        
# 2.

def count_letters(fruit, ch):
    count = 0
    for char in fruit:
        if char == ch:
            count += 1
    print count
    
# 3.

def count_letters(fruit, ch, start=0):
    import string
    count=0
    while start<len(fruit):
        n=string.find(fruit, ch, start)
        if n==-1: start+=1
        else: 
            start=n+1
            count+=1
    return count
    
    
“%s %s %s” % ('this', 'that', 'something')
“%s %s %s %s” % ('yes', 'no', 'up', 'down')
“%d %f %s” % (3, 3, 'three')