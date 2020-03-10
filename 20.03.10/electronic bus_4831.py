# import sys; sys.stdin = open('electronic bus.txt', 'r')

# for tc in range(1, int(input())+1):
#     # K = 한번 충전으로 이동가능한 정류장 수
#     # N = 0번부터 출발해 도착하는 종점의 정류장 번호
#     # M = 충전기 설치된 정류장
#     K, N, M = map(int, input().split())
#     charge_station = list(map(int, input().split()))
#     charge_station.append(N)
#     gas = K
#     stop = 0 # 충전기 정류장 지난 횟수
#     cnt = 0
#     for i in range(1, N):
#         gas -= 1
#         if i in charge_station:
#             if i != charge_station[-1]:
#                 if gas < charge_station[stop+1] - charge_station[stop]:
#                     cnt += 1
#                     gas = K
#                 stop += 1
#         else:
#             if gas == 0:
#                 print(f'#{tc} {0}')
#                 break
#     else:
#         print(f'#{tc} {cnt}')


#
import sys; sys.stdin = open('electronic bus.txt', 'r')

for tc in range(1, int(input())+1):
    K, N, M = map(int, input().split())
    pos = list(map(int, input().split()))

    station = [0] * (N+1)
    for p in pos:
        station[p] = 1

    bus = ans = 0
    while bus + K < N:
        for p in range(bus+K, bus, -1):
            if station[p]:
                bus = p; ans += 1
                break
        else: 
            ans = 0; break
    print(f'#{tc} {ans}')