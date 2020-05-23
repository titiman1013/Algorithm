import sys; sys.stdin = open('samsung bus.txt', 'r')

for tc in range(1, int(input())+1):
    result = [0] * 5000
    N = int(input())
    print(f'#{tc}', end = ' ')
 
    bus_stop = []
    for n in range(N):
        bus_stop.append(list(map(int, input().split())))
     
    station_dict = {}
    P = int(input())
    for p in range(P):
        station = int(input())
        if station not in station_dict:
            station_dict[station] = 0
            for bus in bus_stop:
                if bus[0] <= station <= bus[1]:
                    result[station-1] += 1
        print(f'{result[station-1]}', end = ' ')
    print()
