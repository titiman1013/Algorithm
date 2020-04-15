import sys; sys.stdin = open("rectangle length.txt", "r")

for tc in range(1, int(input())+1):
    arr = list(map(int, input().split()))


    temp = []
    for i in range(len(arr)):
        if arr[i] not in temp:
            temp.append(arr[i])
        else:
            # if temp.count(arr[i]) == 2:
            temp.remove(arr[i])

    print(f'#{tc} {temp[0]}')