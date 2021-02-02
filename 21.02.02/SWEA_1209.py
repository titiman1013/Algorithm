import sys; sys.stdin = open('1209.txt', 'r')

for _ in range(1, 11):
    tc = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    temp = 0
    rd_dia = 0
    ld_dia = 0
    for i in range(100):
        ver = 0
        for j in range(100):
            ver += arr[j][i]
        if temp < max(sum(arr[i]), ver):
            temp = max(sum(arr[i]), ver)
        rd_dia += arr[i][i]
        ld_dia += arr[i][-1 - i]
    answer = max(temp, rd_dia, ld_dia)
    print(f'#{tc} {answer}')