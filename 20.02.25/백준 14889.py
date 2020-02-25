def search(cnt):
    global result
    if cnt == len(check):
        temp = 0
        for i in range(len(check)):
            if check[i] == True:
                temp += 1
        if temp == N//2:
            a_list = []
            b_list = []
            a_team = 0
            b_team = 0
            for i in range(len(check)):
                if check[i] == True:
                    a_list.append(i)
                else:
                    b_list.append(i)
            for i in a_list:
                for j in a_list:
                    if i != j:
                        a_team += arr[i][j]
            for i in b_list:
                for j in b_list:
                    if i != j:
                        b_team += arr[i][j]
            if abs(a_team - b_team) < result:
                result = abs(a_team - b_team)

        return 

    check[cnt] = True
    search(cnt+1)
    check[cnt] = False
    search(cnt+1)




N = int(input())
arr = [list(map(int, input().split())) for i in range(N)]

cnt = 0
check = [False] * N
result = 100000

search(0)
print(result)