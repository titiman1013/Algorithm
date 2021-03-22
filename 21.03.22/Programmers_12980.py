def solution(n):
    # ans = 0
    
    # while n != 1:
    #     if n % 2:
    #         ans += 1
    #         n //= 2
    #     else:
    #         n //= 2

    # return ans + 1

    return bin(n).count('1')





print(solution(5))
print(solution(6))
print(solution(5000))

# answer
# 2
# 2
# 5