def solution(arr):
    answer = []

    for val in arr:
        if answer:
            if answer[-1] == val:
                continue
        answer.append(val)

    return answer




print(solution([1,1,3,3,0,1,1]))
print(solution([4,4,4,3,3]))

# answer
# [1, 3, 0, 1]
# [4, 3]