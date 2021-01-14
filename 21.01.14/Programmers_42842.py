# def solution(brown, yellow):
#     answer = []

#     all = brown + yellow
#     for i in range(min(3, min(brown, yellow)), max(brown, yellow)):
#         if all / i == all // i:
#             if (all // i + i - 2) * 2  == brown and all // i >= i:
#                 answer = [all // i, i]
#                 break

#     return answer



# best solve

def solution(brown, yellow):
    for i in range(1, int(yellow ** (1 / 2)) + 1):
        if yellow % i == 0:
            if (i + yellow // i) * 2 == brown - 4:
                return [yellow // i + 2, i + 2]




print(solution(10, 2))
print(solution(8, 1))
print(solution(24, 24))