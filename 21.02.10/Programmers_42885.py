# false

# from collections import Counter

# def solution(people, limit):
#     answer = 0

#     people_dic = Counter(people)
#     for key1, val1 in people_dic.items():
#         max_sum = 0
#         temp_keys = []
#         for key2, val2 in people_dic.items():
#             if key1 == key2:
#                 if key1 * 2 == limit:
#                     answer += people_dic[key1] // 2
#                     if people_dic[key1] % 2:
#                         people_dic[key1] = 1
#                     else:
#                         people_dic[key1] = 0
#                     continue
            
#             if val1 > 0 and val2 > 0:
#                 if max_sum < key1 + key2 <= limit:
#                     max_sum = key1 + key2
#                     temp_keys = [key1, key2]
        
#         if temp_keys:
#             temp = min(people_dic.get(temp_keys[0]), people_dic.get(temp_keys[1]))
#             answer += temp
#             people_dic[temp_keys[0]] -= temp
#             people_dic[temp_keys[1]] -= temp
    
#     for val in people_dic.values():
#         answer += val

#     return answer


# binary search

def solution(people, limit):
    answer = 0

    answer = len(people)
    people.sort()
    lo, hi = 0, len(people) - 1

    while lo < hi:
        if people[lo] + people[hi] <= limit:
            answer -= 1
            lo += 1
            hi -= 1
        
        else:
            hi -= 1

    return answer






print(solution([70, 50, 80, 50], 100))
print(solution([70, 80, 50], 100))