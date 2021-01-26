from collections import Counter

def solution(citations):
    answer = 0

    citations.sort(reverse=True)
    dic = Counter(citations)
    
    cnt = 0
    for key, val in dic.items():
        cnt += val
        if key >= cnt :
            answer = cnt

    return answer


#

# def solution(citations):
#     answer = 0

#     citations.sort(reverse=True)
#     for idx, citation in enumerate(citations):
#         if idx + 1 <= citation:
#             answer = idx + 1

#     return answer





print(solution([3, 0, 6, 1, 5]))
print(solution([31, 66]))

# answer 
# 3
# 2