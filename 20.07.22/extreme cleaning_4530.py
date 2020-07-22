import sys; sys.stdin = open('extreme cleaning.txt', 'r')

# time error
# for tc in range(1, int(input())+1):
#     start, end = map(int, input().split())

#     res = 0
#     for floor in range(start, end):
#         if floor == 0:
#             continue
#         if '4' not in str(floor):
#             res += 1

#     print(f'#{tc} {res}')


#
for tc in range(1, int(input())+1):
    start, end = map(int, input().split())

    res = 0
    for floor in range(start+1, end+1):
        if floor == 0:
            continue
        if '4' not in str(floor):
            res += 1

    print(f'#{tc} {res}')


# 1의자리 10의자리 100의자리 같이 x10마다 다른 for문으로 break를 걸어 풀어보기