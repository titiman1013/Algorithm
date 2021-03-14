def solution(N, number):
    # answer = 0

    # 8번보다 많이 사용하는 경우는 생각 X
    dp = [set([int(str(N) * i)]) for i in range(1, 9)]
    for i in range(8):
        for j in range(i):
            for p in dp[j]:
                for q in dp[i - j - 1]:
                    dp[i].add(p * q)
                    dp[i].add(p + q)
                    dp[i].add(p - q)
                    if q:
                        dp[i].add(p // q)
        print(dp[i])
        if number in dp[i]:
            return i + 1

    return -1




print(solution(5, 12))
print(solution(2, 11))

# answer
# 4
# 3