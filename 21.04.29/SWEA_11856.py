import sys; sys.stdin = open('11856.txt', 'r')

from collections import Counter

for tc in range(1, int(input()) + 1):
    S = input()
    
    print(f'#{tc}', end=" ")
    counter = Counter(S)
    for key, val in counter.items():
        if val != 2:
            print('No')
            break
    else:
        print('Yes')