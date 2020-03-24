import sys; sys.stdin = open("salary box.txt", "r")

for tc in range(1, int(input())+1):
    N = int(input())
    arr = [list(input().split()) for _ in range(N)]
    
    res = 0
    for i in range(N):
        per = float(arr[i][0])
        pay = int(arr[i][1])
        res += round(per * pay, 6)
    print(f'#{tc} {res}')