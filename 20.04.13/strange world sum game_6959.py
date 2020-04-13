import sys; sys.stdin = open("strange world sum game.txt", "r")

for tc in range(1, int(input())+1):
    arr = input()
    
    res = 0
    while len(arr) != 1:
        res += 1
        temp = 0
        cnt = 0
        for i in range(len(arr)-1):
            if int(arr[i]) + int(arr[i+1]) > temp:
                temp = int(arr[i]) + int(arr[i+1])
                cnt = i
        tail = arr[cnt+2:]
        arr = arr[:cnt]
        arr += (str(temp)+tail)
        print(arr)
    if res % 2:
        res = 'A'
    else:
        res = 'B'
    print(f'#{tc} {res}')