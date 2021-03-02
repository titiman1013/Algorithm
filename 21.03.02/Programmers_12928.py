def solution(n):
    # answer = 0

    # weaknum_set = set()
    # if n == 1: return 1
    # for num in range(1, n//2+1):
    #     # if num not in weaknum_set:
    #     div, mod = divmod(n, num)
    #     if mod == 0:
    #         weaknum_set.add(num)
    #         weaknum_set.add(div)
    #             # if num == div:
    #             #     answer += num
    #             # else:
    #             #     answer += num + div
    # answer = sum(weaknum_set)

    # return answer

    return n + sum([i for i in range(1, (n // 2) + 1) if n % i == 0])




print(solution(12))
print(solution(5))

# answer
# 28
# 6