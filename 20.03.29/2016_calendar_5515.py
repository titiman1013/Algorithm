import sys; sys.stdin = open('2016_calendar.txt', 'r')

for tc in range(1, int(input())+1):
    m, d = map(int, input().split())
    # 1월 1일이 금요일 / 2월을 29일까지
    # 월화수목 ... => 0 1 2 3 ...
    
    list_31 = [1, 3, 5, 7, 8, 10, 12]
    list_30 = [4, 6, 9, 11]
    list_29 = [2]

    start = 4
    # 월 지날때 일수 더해주는 계산
    for i in range(1, m):
        if i in list_31:
            start += 31
        elif i in list_30:
            start += 30
        elif i in list_29:
            start += 29
    start += d

    print(f'#{tc} {(start-1)%7}')

# print((366-1)%7)