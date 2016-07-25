def count_letters(s):
    dict={}
    s.lower()
    for letter in s:
        dict[letter]=dict.get(letter, 0)+1
    #return dict
    letters=dict.items()
    letters.sort()
    for it in letters:
        print it