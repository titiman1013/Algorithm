#

# def solution(N, number):
#     # answer = 0

#     # 8번보다 많이 사용하는 경우는 생각 X
#     dp = [set([int(str(N) * i)]) for i in range(1, 9)]
#     for i in range(8):
#         for j in range(i):
#             for p in dp[j]:
#                 for q in dp[i - j - 1]:
#                     dp[i].add(p * q)
#                     dp[i].add(p + q)
#                     dp[i].add(p - q)
#                     if q:
#                         dp[i].add(p // q)
#         print(dp[i])
#         if number in dp[i]:
#             return i + 1

#     return -1


#

# i와 i-X_i 를 조합했을 때 만들어지는 것이 더해서 i 가 만들어지는 모든 자연수 조합
# (i 가 6 이면 X_i 는 각각 1 2 3 이고, i-X_i 는 5 4 3...) 
# 그런데 -2 를 하는 이유는 zero indexed 라서 S[0] 이 N 을 한 번 써서 만들어진 조합 
# S[1] 이 N을 두 번 써서 만들어진 조합이기 때문에 X_i 에서 부족한 1과 y 쪽에서 부족한 1을 빼서 -2

def solution(N, number):
    if N == number: return 1

    dp = [set(N)]
    for i in range(2, 9):
        lst = [int(str(N) * i)]
        for j in range(i // 2):
            for p in dp[i]:
                for q in dp[i - j - 2]:
                    lst.append(p + q)
                    lst.append(p - q)
                    lst.append(q - p)
                    lst.append(p * q)
                    if p: lst.append(q // p)
                    if q: lst.append(p // q)
        if number in set(lst):
            return i
        dp.append(lst)
    return -1
    




print(solution(5, 12))
print(solution(2, 11))

# answer
# 4
# 3