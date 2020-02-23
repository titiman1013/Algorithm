import sys
sys.stdin = open("스도쿠.txt", "r")

T = int(input())
for t in range(T):
    arr = [list(map(int, input().split())) for i in range(9)]
    
    result = []
    for i in range(9): # 가로
        temp = 0
        for j in range(9):
            temp += arr[i][j]
        if temp != 45:
            result.append('1')
    for i in range(9): # 세로
        temp = 0
        for j in range(9):
            temp += arr[j][i]
        if temp != 45:
            result.append('1')
    for k in range(3): # 칸
        temp = 0
        for i in range(3):
            for j in range(3):
                temp += arr[i+k*3][j+k*3]
        if temp != 45:
            result.append('1')
    if '1' in result:
        print(f'#{t+1} 0')
    else:
        print(f'#{t+1} 1')