# false

# def solution(n,a,b):
#     answer = 1

#     while min(a, b) + 1 != max(a, b):
#         answer += 1
#         a = a // 2 + a % 2
#         b = b // 2 + b % 2
        
#     return answer


#

def solution(n, a, b):
    answer = 0

    # 1, 2 의 경우의 수 차단을 위해 +1
    while a != b:
        a = (a + 1) // 2
        b = (b + 1) // 2
        answer += 1

    return answer




print(solution(8, 4, 7))

# answer
# 3