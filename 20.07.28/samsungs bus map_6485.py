import sys; sys.stdin = open('samsungs bus map.txt', 'r')

for tc in range(1, int(input())+1):
    bus = []
    for i in range(1, int(input())+1):
        bus.append(list(map(int, input().split())))

    res = []
    for p in range(int(input())):
        res.append(0)
        station = int(input())
        for i in range(len(bus)):
            if bus[i][0] <= station <= bus[i][1]:
                res[p] += 1
    
    print(f'#{tc}', end=" ")
    for i in range(len(res)):
        if i == len(res) - 1:
            print(res[i], end="")
        else:
            print(res[i], end=" ")
    print()