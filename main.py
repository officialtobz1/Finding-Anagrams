def find_anagram(word, anagram):
    # [assignment] Add your code here
    if (sorted(word) == sorted(anagram)):
        answer = True
    else:
        answer = False
    print (find_anagram('dormitory', 'dirty room'))
