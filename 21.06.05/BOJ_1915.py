import sys; sys.stdin = open('1915.txt', 'r')

import sys

input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]

answer = 0
for i in range(N):
    for j in range(M):
        if arr[i][j]:
            cnt = 1
            flag = True
            for p in range(min(N - i, M - j)):
                if flag == False: break
                for q in range(min(N - i, M - j)):
                    print((i, j), (p, q), (i + p, j + q), cnt)
                    if arr[i + p][j + q] == 0:
                        flag = False
                        break
                else: 
                    cnt += 1
            if cnt ** 2 > answer and flag:
                answer = cnt ** 2

print(answer)