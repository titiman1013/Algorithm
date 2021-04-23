import sys; sys.stdin = open('1234.txt', 'r')

for tc in range(1, 11):
    N, arr = map(str, input().split())
    arr = list(map(str, arr))
    
    while True:
        for i in range(len(arr) - 1):
            if arr[i] == arr[i + 1]:
                del arr[i + 1]
                del arr[i]
                break
        else:
            break
    
    print(f'#{tc} {"".join(arr)}')