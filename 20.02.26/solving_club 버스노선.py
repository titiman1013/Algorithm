import sys
sys.stdin = open("버스노선.txt", "r")


# T = int(input())
# for t in range(T):
#     stop_list = []
#     MAX = 0
#     N = int(input())
#     for n in range(N):
#         a, b = list(map(int, input().split()))
#         stop_list.append((a,b))
#         if b > MAX:
#             MAX = b

#     P = int(input())
#     for i in range(P):
#         trash = int(input())
    
#     result = []
#     for i in range(MAX):
#         result.append(0)
#     for stop in stop_list:
#         for j in range(stop[0]-1, stop[1]):
#             result[j] += 1
    

#     print(f'#{t+1}', end = ' ')
#     length = len(result)
#     for i in result:
#         if i == length-1:
#             print(f'{i}')
#         else:
#             print(f'{i}', end = ' ')


# T = int(input())
# for t in range(T):
#     result = [0] * 5000
#     MAX = 0
#     N = int(input())
#     print(f'#{t+1}', end = ' ')

#     bus_stop = []
#     for n in range(N):
#         bus_stop.append(list(map(int, input().split())))
#         if bus_stop[-1][-1] > MAX:
#             MAX = bus_stop[-1][-1]
    
#     P = int(input())
#     for p in range(P):
#         station = int(input())
#         for bus in bus_stop:
#             if bus[0] <= station <= bus[1]:
#                 result[station-1] += 1
#         print(f'{result[p]}', end = ' ')
#     print()



T = int(input())
for t in range(T):
    result = [0] * 5000
    N = int(input())
    print(f'#{t+1}', end = ' ')

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