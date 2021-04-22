import sys; sys.stdin = open('1216.txt', 'r')

#

# def horizontal(line, j, answer):
#     for q in range(100 - j):
#         if (q + 1) % 2:
#             if line[:(j + q) // 2] == line[(j + q) // 2 + 1:]:
#                 if q + 1 > answer:
#                     answer = q + 1
#         else:
#             if line[:(j + q) // 2] == line[(j + q) // 2:]:
#                 if q + 1 > answer:
#                     answer = q + 1
#     return answer


# def vertical(arr, i, j, answer):
#     line = ''
#     for idx in range(100 - i):
#         line += arr[i + idx][j]
#     for p in range(100 - i):
#         if (i + p) % 2:
#             if line[:(i + p) // 2] == line[(i + p) // 2 + 1:]:
#                 if p + 1 > answer:
#                     answer = p + 1
#         else:
#             if line[:(i + p) // 2] == line[(i + p) // 2:]:
#                 if p + 1 > answer:
#                     answer = p + 1
#     return answer



# for tc in range(1, 11):
#     answer = 0

#     T = int(input())
#     arr = list(input() for _ in range(100))
#     for i in range(100):
#         for j in range(100):
#             answer = horizontal(arr[i][j:], j, answer)
#             answer = vertical(arr, i, j, answer)

#     print(f'#{tc} {answer}')



#

for _ in range(10):
    answer = 0

    tc = int(input())
    arr = list(input() for _ in range(100))
    result = []

    m = 1
    while m <= 100:
        for i in range(100):
            for j in range(100 - m + 1):
                for k in range(m // 2):
                    if arr[i][j + k] != arr[i][j - k - 100 + m - 1]:
                        break
                else:
                    result = arr[i][j:j + m]
                    if len(result) > answer:
                        answer = len(result)
        m += 1
 
    m = 0
    while m <= 100:
        for i in range(100):
            for j in range(100 - m + 1):
                result = []
                for k in range(m // 2):
                    if arr[j + k][i] != arr[j - k - 100 + m - 1][i]:
                        break
                else:
                    for l in range(m):
                        result.append(arr[j + l][i])
                    if len(result) > answer:
                        answer = len(result)
        m += 1

    print(f'#{tc} {answer}')