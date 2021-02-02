import sys; sys.stdin = open('1220.txt', 'r')

for tc in range(1, 11):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 위가 N, 아래가 S
    # 1이 N, 아래가 2
    answer = 0
    for i in range(N):
        temp = 0
        for j in range(N):
            if arr[j][i] == 1:
                temp = 1
            elif arr[j][i] == 2:
                if temp:
                    answer += 1
                    temp = 0
            
    print(f'#{tc} {answer}')