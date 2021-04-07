# false

# def solution(n, a, b):
#     answer = 1

#     while min(a, b) + 1 != max(a, b):
#         answer += 1
#         a = a // 2 + a % 2
#         b = b // 2 + b % 2
        
#     return answer


#

# def solution(n, a, b):
#     answer = 0

#     # 1, 2 의 경우의 수 차단을 위해 +1
#     while a != b:
#         a = (a + 1) // 2
#         b = (b + 1) // 2
#         answer += 1

#     return answer


# binary search

import math

def solution(n, a, b):
    answer = 0

    a, b = min(a, b), max(a, b)
    answer = int(math.log(n, 2))
    s, e = 1, n
    m = (s + e) // 2
    while True:
        if s <= m and e > m:
            break
        elif s >= m:
            s = m
            m = (s + e) // 2
            answer -= 1
        elif e <= m:
            e = m
            m = (s + e) // 2
            answer -= 1

    return answer




print(solution(8, 4, 7))

# answer
# 3