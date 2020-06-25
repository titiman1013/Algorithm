import sys; sys.stdin = open('road find.txt', 'r')

# 출발점은 0, 도착점은 99
for T in range(10):
    tc, N = map(int, input().split())
    roads = list(map(int, input().split()))

    arr = [[0] for _ in range(N)]

    for i in range(0, N*2, 2):
        arr[roads[i]].append(roads[i+1])
    
    for i in range(N):
        arr[i].pop(0)
    
    # print(arr)

    res = 0
    stack = [0]
    while stack:
        now = stack.pop()
        if arr[now]:
            for i in range(len(arr[now])):
                stack.append(arr[now][i])
                if arr[now][i] == 99:
                    res = 1
                    stack.clear()
                    break
    
    print(f'#{tc} {res}')