import sys; sys.stdin = open("perfect suffle.txt", "r")

for tc in range(1, int(input())+1):
    N = int(input())
    arr = list(input().split())
    
    print(f'#{tc}', end=' ')
    if N % 2:
        for i in range(N//2):
            print(arr[i], end=' ')
            print(arr[N//2+i+1], end=' ')
        print(arr[N//2], end=' ')
    else:
        for i in range(N//2):
            print(arr[i], end=' ')
            print(arr[N//2+i], end=' ')
    print()