from itertools import combinations

def solution(numbers):
    answer = []

    temp = set()
    combs = list(combinations(numbers, 2))
    for comb in combs:
        temp.add(sum(comb))
    answer = list(temp)
    answer.sort()

    return answer




print(solution([2, 1, 3, 4, 1]))
print(solution([5, 0, 2, 7]))