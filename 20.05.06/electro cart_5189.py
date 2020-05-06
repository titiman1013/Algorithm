import sys; sys.stdin = open('electro cart.txt', 'r')
from itertools import permutations

for tc in range(1, int(input())+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    minimum = 1000000
    order = list(permutations(range(2, N+1), N-1))
    for i in range(len(order)):
        temp = 0
        for j in range(len(order[i])):
            if j == 0:
                temp += arr[0][order[i][j]-1]
            else:
                temp += arr[order[i][j-1]-1][order[i][j]-1]
        temp += arr[order[i][-1]-1][0]
        if temp < minimum:
            minimum = temp

    print(f'#{tc} {minimum}')