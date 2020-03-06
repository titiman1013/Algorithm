import sys
sys.stdin = open("시험점수.txt", "r")

# 2
# T = int(input())
# for t in range(T):
#     arr = [list(map(int, input().split())) for i in range(4)]
#     ans = [0] # 0점인 경우
#     for x in arr: # 문제별 점수
#         num = []
#         for y in ans: # 가능한 점수
#             num.append(x+y)
#         ans += num
#     print(f'#{t+1} {len(set(ans))}')

# 3
# T = int(input())
# for t in range(T):
#     N = int(input())
#     arr = list(map(int, input().split()))
#     ans = set([0])
#     for x in arr:
#         num = set()
#         for y in ans:
#             num.add(x+y)
#         ans = set(list(ans)+list(num))
#     print(f'#{t+1} {len(set(ans))}')

# 4
T = int(input())
for t in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    total = sum(arr)
    s = [0] * (total+1)
    s[0] = 1
    for x in arr:  # x점 문제에 대해
        for i in range(total-x, -1, -1):
            if s[i] == 1:  # i점이 가능하면
                s[i+x] = 1  # i+x점도 가능
    print(f'#{t+1} {sum(s)}')