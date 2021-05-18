import sys; sys.stdin = open('2485.txt', 'r')

from math import gcd

for tc in range(1, int(input()) + 1):
    N = int(input())
    trees = list(int(input()) for _ in range(N))

    answer = 0
    distances = list()
    for i in range(len(trees) - 1):
        distances.append(trees[i + 1] - trees[i])

    min_length = distances[0]
    for dis in distances[1:]:
        min_length = gcd(min_length, dis)
    
    for i in range(len(trees) - 1):
        answer += (trees[i + 1] - trees[i]) // min_length - 1

    print(answer)