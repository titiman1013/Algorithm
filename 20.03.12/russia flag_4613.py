import sys; sys.stdin = open('russia flag.txt', 'r')

for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]
    
    cnt = 0
    color = 0   # 0이면 흰색 1이면 파란색 2이면 빨간색 칠하기
    for i in range(N):
        color_cnt = {'W': 0, 'B': 0, 'R': 0}
        for j in range(M):
            if arr[i][j] == 'W':
                color_cnt['W'] += 1
            elif arr[i][j] == 'B':
                color_cnt['B'] += 1
            else:
                color_cnt['R'] += 1
        if i == 0:  # 첫줄은 무조건 흰색
            cnt = M - color_cnt['W']
        else:
            