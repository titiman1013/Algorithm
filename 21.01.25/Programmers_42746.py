# time error

from itertools import permutations

def solution(numbers):
    answer = ''

    max = 0
    number_lst = list(set(permutations(numbers, len(numbers))))
    for number in number_lst:
        temp = ''
        for num in number:
            temp += str(num)
        if int(temp) > max:
            max = int(temp)
    answer = str(max)

    return answer




print(solution([6, 10, 2]))
print(solution([3, 30, 34, 5, 9]))

# answer
# 6210
# 9534330