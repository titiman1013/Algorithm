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

    rocks.sort()
    rocks.append(distance)
    s, e = 0, distance

    while s <= e:
        m = (s + e) // 2
        pre = 0
        mins = distance
        cnt = 0

        for i in range(len(rocks)):
            if rocks[i] - pre < m:
                cnt += 1
            else:
                mins = min(mins, rocks[i] - pre)
                pre = rocks[i]

        if cnt > n:
            e = m - 1
        else:
            answer = mins
            s = m + 1

    return answer



print(solution(25, [2, 14, 11, 21, 17], 2))