# # time error

# from itertools import permutations

# def solution(numbers):
#     answer = ''

#     max = 0
#     number_lst = list(set(permutations(numbers, len(numbers))))
#     for number in number_lst:
#         temp = ''
#         for num in number:
#             temp += str(num)
#         if int(temp) > max:
#             max = int(temp)
#     answer = str(max)

#     return answer


#

def solution(numbers):
    answer = ''

    numbers = list(map(str, numbers))
    # 문자열 비교연산은 앞자리부터 ascii코드로 진행되며, 1000이하의 수가 조건이기 때문에 *3을 해준다
    numbers.sort(key=lambda x: x * 3, reverse=True)
    answer += str(int(''.join(numbers)))

    return answer




print(solution([6, 10, 2]))
print(solution([3, 30, 34, 5, 9]))

# answer
# 6210
# 9534330