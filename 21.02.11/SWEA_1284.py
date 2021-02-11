import sys; sys.stdin = open('1284.txt', 'r')

for tc in range(1, int(input()) + 1):
    # P: A사 1L당 요금, Q: B사 R리터 이하 요금, R: B사 요금제한, S: B사 1L당 요금, W: 수도 사용 양
    P, Q, R, S, W = map(int, input().split())

    a_bill = P * W
    if W <= R:
        b_bill = Q
    else:
        b_bill = Q + (W - R) * S
    print(f'#{tc} {min(a_bill, b_bill)}')