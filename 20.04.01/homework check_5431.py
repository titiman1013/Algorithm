import sys; sys.stdin = open("homework check.txt", "r")

for tc in range(1, int(input())+1):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))

    check = [0] * N
    for i in range(K):
        check[arr[i]-1] = 1

    res_list = []
    for i in range(N):
        if check[i] == 0:
            res_list.append(i+1)
    
    print(f'#{tc}', end=' ')
    for i in range(len(res_list)):
        print(res_list[i], end=' ')
    print()