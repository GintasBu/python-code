def find(str, ch, start=0, end=0):
    index = start
    if end==0: end=len(str)
    while index < end:
        if str[index] == ch:
            return index
        index = index + 1
    return -1