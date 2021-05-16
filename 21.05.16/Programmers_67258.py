# false

from collections import Counter

def solution(gems):
    answer = []

    gems_counter = Counter(gems)
    N = len(gems_counter)
    if N == 1:
        answer = [1, 1]
    elif N == len(gems):
        answer = [1, len(gems)]
    else:
        s, e = 0, len(gems)
        while s <= e:
            if len(Counter(gems[s:e - 1])) == N:
                e -= 1
            elif len(Counter(gems[s + 1:e])) == N:
                s += 1
            else:
                answer = [s + 1, e]
                break

    return answer




print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))
print(solution(["AA", "AB", "AC", "AA", "AC"]))
print(solution(["XYZ", "XYZ", "XYZ"]))
print(solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"]))
print(solution(['E', 'F', 'A', 'F', 'F', 'B', 'A', 'E', 'E', 'E']))

# answer
# [3, 7]
# [1, 3]
# [1, 1]
# [1, 5]