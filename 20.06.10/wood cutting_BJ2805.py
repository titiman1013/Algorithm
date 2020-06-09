import sys; sys.stdin = open('wood cutting.txt', 'r')

for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    arr.sort()
    height = max(arr)
    temp = 0
    while True:
        for i in range(len(arr)-1, -1, -1):
            if arr[i] > height: 
                temp += (arr[i] - height)
            else:
                break
        if temp <= M:
            res = height
            temp = 0
            height -= 1
        else:
            break

    print(f'#{tc} {res}')