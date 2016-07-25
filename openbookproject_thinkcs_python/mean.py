import sys
import string
nums=sys.argv[1:]
#print float(nums[0])
S=0
L=0
for i in range(len(nums)):   
    S+=float(nums[i])
    L+=1
#print sum(list(nums))/len(list(nums))
print S/L