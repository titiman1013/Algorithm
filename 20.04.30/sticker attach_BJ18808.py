import sys; sys.stdin = open('sticker attach.txt', 'r')

#
# for tc in range(1, int(input())+1):
#     N, M, K = map(int, input().split())
#     # N은 가로 M은 세로 K는 스티커 개수
#     stickers_arr = []
#     for i in range(K):
#         R, C = map(int, input().split())
#         # 스티커 행의 개수, 열의 개수
#         for j in range(R):
#             stickers_arr.append([list(map(int, input().split())) for _ in range(R)])


# #
# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]

# def rotate():
#     pass


# for tc in range(1, int(input())+1):
#     N, M, K = map(int, input().split())
    
#     arr = [[0] * M for _ in range(N)]

#     for i in range(K):
#         R, C = map(int, input().split())
#         sticker = [list(map(int, input().split())) for _ in range(R)]
        
#         # 적합한 스티커인지 확인
#         select = True
#         # 가로 확인
#         for p in range(R):
#             if sum(sticker[p]) == 0:
#                 select = False
#                 break
#         # 가로 통과했다면 세로 확인
#         if select == True:
#             for q in range(C):
#                 temp = 0
#                 for p in range(R):
#                     if sticker[p][q] == 0:
#                         temp += 1
#                 if temp == R:
#                     select = False
#                     break
#         # 다 이어져 있는지
#         if select == True:
#             pass
#         # 적합한 스티커이면 이제 스티커 넣기
#         if select == True:
#             print('check')
#     print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')


#
# 시계방향으로 90도 회전한 배열을 반환한다.
def rotate_90(array):
    ver, hor = len(array), len(array[0])
    new_array = [[array[-j + ver - 1][i] for j in range(ver)] for i in range(hor)]
    return new_array
 
 
# 스티커를 붙일 수 있다면 True, 아니라면 False를 반환한다.
def check(x, y, sticker_array):
    r, c = len(sticker_array), len(sticker_array[0])
    for i in range(r):
        for j in range(c):
            if sticker_array[i][j] == 0:
                continue
            elif laptop[x + i][y + j] == 1:
                return False  # 겹치는 부분 있음
    return True  # 스티커 붙일 수 있다.
 
 
# laptop에 스티커를 붙인다.
def attach(x, y, sticker_array):
    r, c = len(sticker_array), len(sticker_array[0])
    for i in range(r):
        for j in range(c):
            if sticker_array[i][j] == 1:
                laptop[x + i][y + j] = 1
 
 
for tc in range(1, int(input())+1):
    n, m, k = map(int, input().split())  # 세로(n), 가로(m), 스티커개수(k)
    laptop = [[0] * m for _ in range(n)]
    sticker = [{} for _ in range(k)]
 
    for i in range(k):
        sticker[i]['r'], sticker[i]['c'] = map(int, input().split())
        sticker[i]['board'] = [list(map(int, input().split())) for _ in range(sticker[i]['r'])]
 
    for num in range(k):
        cnt = 0  # 회전한 횟수. 3번보다 더 많이 회전할 순 없다.
        r, c = sticker[num]['r'], sticker[num]['c']
        board = sticker[num]['board']
        while cnt < 4:
            if r > n or c > m:  # 크기 비교
                r, c, board = c, r, rotate_90(board)
                cnt += 1
                continue
            success = 0
            for i in range(0, n - r + 1):
                for j in range(0, m - c + 1):
                    if not check(i, j, board): continue
                    ## 스티커를 붙일 수 있다면?
                    attach(i, j, board)
                    success = 1
                    break
                if success: break
            if success:
                break
            else:
                r, c, board = c, r, rotate_90(board)
                cnt += 1
 
    anv = 0
    for i in range(n):
        for j in range(m):
            if laptop[i][j] == 1: anv += 1
            
    print(f'#{tc} {anv}')