import sys; sys.stdin = open('4676.txt', 'r')

from collections import Counter

for tc in range(1, int(input()) + 1):
    strings = input()
    H = int(input())
    positions = list(map(int, input().split()))
    answer = ''

    pos_dict = Counter(positions)
    for idx, string in enumerate(strings):
        if pos_dict.get(idx):
            for _ in range(pos_dict.get(idx)):
                answer += '-'
        answer += string
    if pos_dict.get(len(strings)):
        for _ in range(pos_dict.get(len(strings))):
            answer += '-'

    print(f'#{tc} {answer}')