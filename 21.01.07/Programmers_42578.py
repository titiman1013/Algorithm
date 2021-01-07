# first solve

# def solution(clothes):
#     hash_map = {}
#     for cloth in clothes:
#         if cloth[1] in hash_map:
#             hash_map[cloth[1]] += 1
#         else:
#             hash_map[cloth[1]] = 1
    
#     answer = 0
#     for val in hash_map.values():
#         if answer:
#             answer *= (val + 1)
#         else:
#             answer = val + 1
    
#     return answer - 1
    
    
    
    # answer = 0
    # return answer



# best solve

from collections import Counter
from functools import reduce

def solution(clothes):
    return reduce(lambda x, y: x * y, [val + 1 for val in Counter([cloth[1] for cloth in clothes]).values()]) - 1




print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))
print(solution([["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]))

# answer

# 5
# 3