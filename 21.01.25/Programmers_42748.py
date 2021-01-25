def manufacture(array, i, j, k):
    arr = sorted(array[i - 1:j])
    return arr[k - 1]



def solution(array, commands):
    answer = []

    for i, j, k in commands:
        answer.append(manufacture(array, i, j, k))

    return answer




print(solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))

# answer
# [5, 6, 3]