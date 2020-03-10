import sys; sys.stdin = open('crop.txt', 'r')

for tc in range(1, int(input())+1):
    N = int(input())
    arr = [list(map(int, list(input()))) for i in range(N)]
    
    s = e = N // 2
    ans = 0
    for row in range(N):
        for i in range(s, e + 1):
            ans += arr[row][i]
        
        if row < N // 2: s, e = s - 1, e + 1
        else: s, e = s + 1, e - 1

    print(f'#{tc} {ans}')