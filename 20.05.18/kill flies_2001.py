import sys; sys.stdin = open('kill flies.txt', 'r')

for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    res = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
        # +1 해주지 않으면 가장 끝열을 세지 않음
            temp = 0
            for p in range(M):
                for q in range(M):
                    temp += arr[i+p][j+q]
            if res < temp:
                res = temp
    
    print(f'#{tc} {res}')