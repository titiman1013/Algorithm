# def solution(cacheSize, cities):
#     answer = 0

#     if cacheSize == 0:
#         return len(cities) * 5

#     cache = []
#     for city in cities:
#         city = city.lower()
#         if not city in cache:
#             if len(cache) < cacheSize:
#                 cache.append(city)
#             else:
#                 cache.pop(0)
#                 cache.append(city)
#             answer += 5
#         else:
#             cache.pop(cache.index(city))
#             cache.append(city)
#             answer += 1

#     return answer


# use deque(maxlen)

from collections import deque

def solution(cacheSize, cities):
    answer = 0

    cache = deque(maxlen=cacheSize)
    for city in cities:
        city = city.lower()
        if city in cache:
            cache.remove(city)
            cache.append(city)
            answer += 1
        else:
            cache.append(city)
            answer += 5
    
    return answer




print(solution(3, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))
print(solution(3, ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]))
print(solution(2, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]))
print(solution(5, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]))
print(solution(2, ["Jeju", "Pangyo", "NewYork", "newyork"]))
print(solution(0, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))

# answer
# 50
# 21
# 60
# 52
# 16
# 25