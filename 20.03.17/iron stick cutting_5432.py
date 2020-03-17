import sys; sys.stdin = open("iron stick cutting.txt", "r")

# for tc in range(1, int(input())+1):
#     arr = input()

#     stack = 0
#     res = 0
#     for i in range(len(arr)):
#         if arr[i] == ')':
#             if arr[i-1] == '(':    # 레이저일 경우
#                 stack -= 1
#                 res += stack
#             else:   # 레이저 아닐경우
#                 stack -= 1
#                 res += 1
#         else:
#             stack += 1
                
#     print(f'#{tc} {res}')

#
T = int(input())
for tc in range(1, T+1):
    s = input()
    cnt = 0     # 자른 전체 조각
    stick = 0   # 겹쳐진 쇠막대 개수
    for i in range(len(s)):
        if s[i] == '(':
            stick += 1      # 겹쳐진 쇠 막대 수
        elif s[i] == ')' and s[i-1] == '(':     # 레이저인 경우
            stick -= 1      # 이전의 '('는 레이저이므로 막대에서 제외
            cnt += stick    # 겹쳐진 쇠 막대 만큼 조각이 증가
        else:       # 쇠막대 끝
            cnt += 1    # 조각이 하나 늘고
            stick -= 1  # 겹쳐진 막대가 하나 줄어든 것임
    print('#{} {}'.format(tc, cnt))