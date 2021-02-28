import math

def solution(n):
    # answer = 0

    # for i in range(2, n+1):
    #     for j in range(2, int(math.sqrt(i)) + 1):
    #         if i % j == 0: break
    #     else: answer += 1

    # return answer


    num = set(range(2, n+1))

    for i in range(2, int(math.sqrt(n)) + 1):
        if i in num:
            num -= set(range(i*i, n+1, i))
    
    return len(num)




print(solution(10))
print(solution(5))

# answer
# 4
# 3