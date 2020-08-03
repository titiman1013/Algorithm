import sys; sys.stdin = open('view.txt', 'r')


for tc in range(1, 11):
    N = int(input())
    arr = list(map(int, input().split()))

    res = 0
    for i in range(2, N-2):
        if arr[i] > arr[i-2] and arr[i] > arr[i-1] and arr[i] > arr[i+1] and arr[i] > arr[i+2]:
            temp = []
            temp.append(arr[i-2])
            temp.append(arr[i-1])
            temp.append(arr[i+1])
            temp.append(arr[i+2])
            
            res += arr[i] - max(temp)

    print(f'#{tc} {res}')