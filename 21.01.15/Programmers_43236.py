# permutations time error

# from itertools import permutations

# def solution(distance, rocks, n):
#     answer = set()

#     rocks.sort()
#     per_rocks = list(permutations(rocks, n))
#     for del_rock1, del_rock2 in per_rocks:
#         min = max(rocks)
#         pre = 0
#         for i in range(len(rocks)):
#             if rocks[i] == del_rock1 or rocks[i] == del_rock2: continue
#             else:
#                 dis = rocks[i] - pre
#                 if dis < min:
#                     min = dis
#                 pre = rocks[i]
#         answer.add(min)

#     return max(answer)



# binary search

def solution(distance, rocks, n):
    answer = 0

    

    return answer




print(solution(25, [2, 14, 11, 21, 17], 2))