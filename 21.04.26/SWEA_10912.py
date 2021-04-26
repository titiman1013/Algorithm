import sys; sys.stdin = open('10912.txt', 'r')

from collections import Counter

for tc in range(1, int(input()) + 1):
    strings = input()
    answer = ''

    result = []
    str_counter = Counter(strings)
    for string, cnt in str_counter.items():
        if cnt % 2:
            result.append(string)
    
    if result:
        answer = "".join(sorted(result))
    else:
        answer = 'Good'

    print(f'#{tc} {answer}')