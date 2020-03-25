import sys; sys.stdin = open("7 3 5 game.txt", "r")

def f(cnt):
    if cnt == 7:
        temp = 0
        temp_list = []
        for i in range(len(arr)):
            if check[i] == 1:
                temp_list.append(i)
        if len(temp_list) == 3:
            for i in temp_list:
                temp += arr[i]
            res_list.append(temp)
        return

    check[cnt] = 1
    f(cnt+1)
    check[cnt] = 0
    f(cnt+1)



for tc in range(1, int(input())+1):
    arr = list(map(int, input().split()))
    check = [0] * len(arr)
    res_list = []
    f(0)
    res_list = list(set(res_list))
    res_list.sort()
    print(f'#{tc} {res_list[-5]}')