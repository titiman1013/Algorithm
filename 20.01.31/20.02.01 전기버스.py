import sys
sys.stdin = open("elec bus.txt", "r")

for T in range(int(input())):
    first = list(map(int, input().split()))
    station = list(map(int, input().split()))
    station.append(station[-1]+1)
    gas = first[0]
    charge = 0
    for move in range(first[1]):
        gas -= 1
        if move+1 == first[1]:
            continue
        # if move+1 < first[1]:
        else:
            if move in station:
                if gas < station[move+1] - station[move]:
                    gas += first[0]
                    charge += 1
        if gas == 0:
            charge = 0
            break
    
    print(f'#{T+1} {charge}')