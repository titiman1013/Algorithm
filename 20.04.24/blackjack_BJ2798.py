import sys; sys.stdin = open("blackjack.txt", "r")

# 시간초과
# def select(cnt):
#     global mino
#     global res
#     if cnt == len(arr):
#         temp = 0
#         card_cnt = 0
#         for i in range(len(arr)):
#             if check[i] == True:
#                 temp += arr[i]
#                 card_cnt += 1
#         if card_cnt != 3:
#             return
#         if abs(M - temp) < mino:
#             mino = abs(M - temp)
#             res = temp
#         return

#     check[cnt] = True
#     select(cnt+1)
#     check[cnt] = False
#     select(cnt+1)

# # 시간초과
# def select(cnt, card_cnt, card_sum):
#     global mino
#     global res
#     if cnt == len(arr):
#         if card_cnt != 3:
#             return
#         if card_sum > M:
#             return
#         if abs(M - card_sum) < mino:
#             mino = abs(M - card_sum)
#             res = card_sum
#         return
    
#     check[cnt] = True
#     select(cnt+1, card_cnt+1, card_sum+arr[cnt])
#     check[cnt] = False
#     select(cnt+1, card_cnt, card_sum)

# 위 두개 함수 사용, 재귀
# for tc in range(1, int(input())+1):
#     N, M = map(int, input().split())
#     arr = list(map(int, input().split()))
    
#     check = [False] * len(arr)
#     res = 0
#     mino = 100000
#     # select(0)
#     select(0, 0, 0)

#     # print(f'#{tc} {res}')
#     print(res)


# # 모듈호출
# from itertools import combinations

# for tc in range(1, int(input())+1):
#     N, M = map(int, input().split())
#     arr = list(map(int, input().split()))

#     res = 0
#     mino = 1000000
#     for i in list(combinations(arr, 3)):
#         # print(sum(i))
#         if sum(i) <= M:
#             if abs(M - sum(i)) < mino:
#                 mino = abs(M - sum(i))
#                 res = sum(i)
#                 # print('d')
    
#     print(res)   
#     print(f'#{tc} {res}')
    

# 완전탐색
for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    cards = list(map(int, input().split()))

    result = 0
    for i in range(N):
        for j in range(i+1, N):
            for k in range(j+1, N):
                tot = cards[i] + cards[j] + cards[k]
                if result < tot <= M:
                    result = tot

    # print(result)
    print(f'#{tc} {result}')




# 답
#1 21
#2 497