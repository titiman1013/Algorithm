import sys; sys.stdin = open('code creater.txt', 'r')

# from collections import deque 

for tc in range(1, 11):
    T = int(input())
    arr = list(map(int, input().split()))
    minus = 1
    while True:
        if arr[0] - minus > 0:
            temp = arr.pop(0)
            arr.append(temp - minus)
            if minus == 5:
                minus = 0
            minus += 1
        else:
            # print('hi')
            arr.pop(0)
            arr.append(0)
            break

    print(f'#{tc}', end=" ")
    for i in range(len(arr)):
        print(f'{arr[i]}', end=" ")
    print()