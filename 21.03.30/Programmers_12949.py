def solution(arr1, arr2):
    answer = [[]]

    l, m, n = len(arr1), len(arr1[0]), len(arr2[0])
    answer = [[0] * n for _ in range(l)]
    for i in range(l):
        for j in range(n):
            temp = 0
            for p in range(m):
                temp += arr1[i][p] * arr2[p][j]
            answer[i][j] = temp

    return answer


    # return [[sum(a * b for a, b in zip(arr1_row, arr2_col)) for arr2_col in zip(*arr2)] for arr1_row in arr1]




print(solution([[1, 4], [3, 2], [4, 1]], [[3, 3], [3, 3]]))
print(solution([[2, 3, 2], [4, 2, 4], [3, 1, 4]], [[5, 4, 3], [2, 4, 1], [3, 1, 1]]))

# answer
# [[15, 15], [15, 15], [15, 15]]
# [[22, 22, 11], [36, 28, 18], [29, 20, 14]]