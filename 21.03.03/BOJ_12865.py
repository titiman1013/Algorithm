import sys; sys.stdin = open('12865.txt', 'r')

#  time error

# def reculsive(idx, weight, satis):
#     global answer

#     if idx == N:
#         if weight <= K:
#             if satis > answer:
#                 answer = satis
#         return

#     reculsive(idx+1, weight+loads[idx][0], satis+loads[idx][1])
#     reculsive(idx+1, weight, satis)



# # N: 물건 개수, K: 들 수 있는 무게
# N, K = map(int, input().split())
# # W: 물건 무게, V: 가치
# loads = [list(map(int, input().split())) for _ in range(N)]

# answer = 0
# reculsive(0, 0, 0)
# print(answer)

# answer
# 14




# dp

# N: 물건 개수, K: 들 수 있는 무게
N, K = map(int, input().split())
# W: 물건 무게, V: 가치
stuff = [[0, 0]] + [list(map(int, input().split())) for _ in range(N)]

answer = 0
knapsack = [[0] * (K + 1) for _ in range(N + 1)]

for i in range(1, N+1):
    for j in range(1, K+1):
        weight, value = stuff[i]
        if j < weight:
            knapsack[i][j] = knapsack[i-1][j]
        else:
            knapsack[i][j] = max(value + knapsack[i-1][j-weight], knapsack[i-1][j])

print(knapsack[N][K])