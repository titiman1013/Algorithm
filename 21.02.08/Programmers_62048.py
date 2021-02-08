import math

def solution(w,h):
    answer = 1

    answer = w * h - (w + h - math.gcd(w, h))

    return answer




print(solution(8, 12))

# answer
# 80