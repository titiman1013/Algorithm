# false

def solution(n,a,b):
    answer = 1

    while min(a, b) + 1 != max(a, b):
        answer += 1
        a = a // 2 + a % 2
        b = b // 2 + b % 2
        
    return answer




print(solution(8, 4, 7))

# answer
# 3