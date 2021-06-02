import sys; sys.stdin = open('1398.txt', 'r')

coins = [1, 10, 25]
dp = [float('inf') for _ in range(100)]
dp[0] = 0

# 1^100 단위별로 1 -> 100, 10 -> 1000, 25 -> 2500 이 된다는 개념
for cost in range(100):
    for coin in coins:
        if cost + coin >= 100: continue
        dp[cost + coin] = min(dp[cost + coin], dp[cost] + 1)

for tc in range(1, int(input()) + 1):
    car_cost = int(input())

    answer = 0
    while car_cost:
        answer += dp[car_cost % 100]
        car_cost //= 100
    
    print(answer)