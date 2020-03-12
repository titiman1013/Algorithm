import sys; sys.stdin = open('russia flag.txt', 'r')

for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]
    
    color = 0   # 0이면 흰색 1이면 파란색 2이면 빨간색 칠하기
    for i in range(N):
        for j in range(M):
            arr[i][j]
            