from collections import Counter

def solution(nums):
    answer = 0

    species = Counter(nums)
    select_cnt = len(nums) // 2
    if len(species) >= select_cnt:
        answer = select_cnt
    else:
        answer = len(species)

    return answer

    # return min(len(nums) // 2, len(set(nums)))




print(solution([3,1,2,3]))
print(solution([3,3,3,2,2,4]))
print(solution([3,3,3,2,2,2]))

# answer
# 2
# 3
# 2