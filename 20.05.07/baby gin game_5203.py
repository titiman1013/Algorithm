import sys; sys.stdin = open('baby gin game.txt', 'r')

# 문제를 읽자 ㅎㅎ
# for tc in range(1, int(input())+1):
#     cards = list(map(int, input().split()))

#     # 마지막으로 받은 카드, run 숫자세기/ +중인지 -중인지, triplet 숫자세기
#     A_player = [0, [0, ''], 0]
#     B_player = [0, [0, ''], 0]

#     for i in range(len(cards)):
#         if i % 2 == 0:
#             # triplet
#             if A_player[2] == 0 or A_player[0] == cards[i]:
#                 A_player[2] += 1
#             else:
#                 A_player[2] = 0
#             # run
#             if A_player[1][0] == 0 or A_player[0] == cards[i] + 1 or A_player[0] == cards[i] -1:
#                 if A_player[1][0] == 0:
#                     A_player[1][0] += 1
#                 elif A_player[1][0] == 1:                    
#                     if A_player[0] == cards[i] + 1:
#                         A_player[1][0] += 1
#                         A_player[1][1] = '+'
#                     else:
#                         A_player[1][0] += 1
#                         A_player[1][1] = '-'
#                 else:
#                     if A_player[0] == cards[i] + 1 and A_player[1][1] == '+':
#                         A_player[1][0] += 1
#                     elif A_player[0] == cards[i] - 1 and A_player[1][1] == '-':
#                         A_player[1][0] -= 1
#             else:
#                 A_player[1] = [0, '']
#             # 마지막카드 갱신
#             A_player[0] = cards[i]
#             # 검사
#             if A_player[1][0] == 3 or A_player[2] == 3:
#                 res = 521290 395020


#
for tc in range(1, int(input())+1):
    cards = list(map(int, input().split()))

    A_player = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
    B_player = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}

    res = 0
    for i in range(len(cards)):
        if i % 2:
            B_player[cards[i]] += 1
            if B_player[cards[i]] == 3:
                res = 2
                break
        else:
            A_player[cards[i]] += 1
            if A_player[cards[i]] == 3:
                res = 1
                break
        temp_A = 0
        temp_B = 0
        for j in range(10):
            if A_player[j] != 0:
                temp_A += 1
            else:
                temp_A = 0
            if B_player[j] != 0:
                temp_B += 1
            else:
                temp_B = 0
            if temp_A == 3 and temp_B == 3:
                res = 3
            elif temp_A == 3:
                res = 1
                break
            elif temp_B == 3:
                res = 2
                break
        if res:
            break
    if res != 3:
        print(f'#{tc} {res}')
    else:
        print(f'#{tc} {0}')