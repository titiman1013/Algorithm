import sys; sys.stdin = open("fly between trains.txt", "r")

for tc in range(1, int(input())+1):
    D, A, B, F = map(int, input().split())

    # 떨어진 거리 D = 250
    # 기차 A 시속 A = 10
    # 기차 B 시속 B = 15
    # 파리 시속 F = 20

    res = D / (A + B) * F
    print(f'#{tc} {res}')