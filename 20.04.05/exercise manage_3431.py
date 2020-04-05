import sys; sys.stdin = open("exercise manage.txt", "r")

for tc in range(1, int(input())+1):
    L, U, X = map(int, input().split())
    
    if X < L:
        res = L - X
    elif L <= X <= U:
        res = 0
    else:
        res = -1
    
    print(f'#{tc} {res}')