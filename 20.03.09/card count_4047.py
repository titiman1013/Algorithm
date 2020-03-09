import sys; sys.stdin = open('card count.txt', 'r')

# 1
# for tc in range(1, int(input().split()) + 1):
#     arr = input()
#     # 필요한 카드 개수
#     cnt = [13] * 4  # 0번: 스페이드, ...3번: 클로버, 무늬별 필요한 카드 수

#     # 개별 카드 정보를 식별, 3개씩 읽어오기
#     cards = set()
#     for i in range(0, len(arr), 3): # 카드의 시작위치
#         tmp = arr[i: i + 3] # 카드 중복 체크를 위해서
#         if tmp in cards: 
#             print('ERROR'); break # ERROR
#         if tmp[0] == 'S':
#             cnt[0] -= 1
#         elif tmp[0] == 'D':
#             cnt[1] -= 1
#         elif tmp[0] == 'H':
#             cnt[2] -= 1
#         else: cnt[3] -= 1
    
#     else:
#         print()


# 2
dict = {'S': 0, 'D': 1, 'H': 2, 'C': 3}

for tc in range(1, int(input().split()) + 1):
    arr = input()
    # 필요한 카드 개수
    cnt = [13] * 4  # 0번: 스페이드, ...3번: 클로버, 무늬별 필요한 카드 수
    check = [[0] * 13 for _ in range(4)]

    for i in range(0, len(arr), 3): # 카드의 시작위치
        a = dict[arr[i]]
        b = int(arr[i + 1]) * 10 + int(arr[i + 2])
        if check[a][b]: break
        check[a][b] = 1
        cnt[a] -= 1
    else:
        print(cnt)