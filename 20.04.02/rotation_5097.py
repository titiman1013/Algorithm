import sys; sys.stdin = open("rotation.txt", "r")

for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    res = M % N
    print(f'#{tc} {arr[res]}')