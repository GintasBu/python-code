import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line


def mapper(record):
    # key: document identifier
    # value: document contents

    # enter sizes:
    l1=5 # initial number of lines in matrix A
    l2=5 # initial number of columns in matrix A
    k1=5 # initial number of lines in matrix B
    k2=5 # initial number of columns in matrix B
    
    if record[0]=="a":
        if record[1]>l1: l1=record[1]
        if record[2]>l2: l2=record[2]
        for l in range(l1):
            for k in range(k2):
                if record[1]==l:
                    key = l, k
                    value=record[0], record[2], record[3]
                    mr.emit_intermediate(key, value)
    else:
        if record[1]>k1: k1=record[1]
        if record[2]>k2: k2=record[2]
        for l in range(l1):
            for k in range(k2):
                if record[2]==k:
                    key = l, k
                    value=record[0], record[1], record[3]
                    mr.emit_intermediate(key, value)


def reducer(key, list_of_values):
    l1=5 # initial number of lines in matrix A
    k2=5 # initial number of columns in matrix B
    S=0
    Sa=[0]*l1
    Sb=[0]*k2
    L=len(list_of_values)
    for z in range(L):
        if list_of_values[z][0]=="a": 
            for l in range(l1):
                if list_of_values[z][1]==l:
                    Sa[l]=list_of_values[z][2]
        else:
            for k in range(k2):
                if list_of_values[z][1]==k:
                    Sb[k]=list_of_values[z][2]
            

    L2=len(Sa)
    for j in range(L2):
        S=S+Sa[j]*Sb[j]
    
    mr.emit((key[0], key[1], S))


# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
