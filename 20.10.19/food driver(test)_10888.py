import sys; sys.stdin = open('food driver.txt', 'r')

from itertools import combinations

for tc in range(1, int(input()) + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    
    stores = []
    homes = []
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                homes.append((i, j))
            elif arr[i][j] > 1:
                stores.append((i, j))
    # print(stores)
    # print(homes)
    
    res_list = []
    for i in range(1, len(stores) + 1):
        c = list(combinations(stores, i))
        # print(c)
        # res = 0
        # for p in range(len(homes)):
        #     res += (abs(homes[p][0] - c[0][0]) + abs(homes[p][1] - c[0][1]))
        # res_list.append(res)
        for storelist in c:
            res = 0
            # print(storelist)
            for home in homes:
                d = 999999
                for store in storelist:
                    d = min(d, abs(home[0] - store[0]) + abs(home[1] - store[1]))
                    # print(arr[store[0]][store[1]])
                res += d
            for store in storelist:
                res += arr[store[0]][store[1]]
            res_list.append(res)

    print(f'#{tc} {min(res_list)}')