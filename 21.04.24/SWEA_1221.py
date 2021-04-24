import sys; sys.stdin = open('1221.txt', 'r')

from collections import Counter

for tc in range(1, int(input()) + 1):
    test_case, N = map(str, input().split())
    arr = list(input().split())
    
    arr_counter = Counter(arr)
    seqs = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']
    
    print(test_case)
    for seq in seqs:
        if arr_counter.get(seq):
            for _ in range(arr_counter.get(seq)):
                print(seq, end=' ')
    print()