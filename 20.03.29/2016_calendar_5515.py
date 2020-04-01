import sys; sys.stdin = open('2016_calendar.txt', 'r')

for tc in range(1, int(input())+1):
    m, d = map(int(input().split()))
    # 1월 1일이 금요일 / 2월을 29일까지
    # 월화수목 ... => 0 1 2 3 ...
    if m <= 2:
        