import sys; sys.stdin = open('1486.txt', 'r')

from itertools import combinations

for tc in range(1, int(input()) + 1):
    N, B = map(int, input().split())
    H = list(map(int, input().split()))

    answer = 10000
    for i in range(1, N + 1):
        clusters = list(combinations(H, i))
        for cluster in clusters:
            if sum(cluster) >= B and sum(cluster) - B < answer:
                answer = sum(cluster) - B
    
    print(f'#{tc} {answer}')