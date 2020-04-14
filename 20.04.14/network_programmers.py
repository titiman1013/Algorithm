def solution(n, computers):
    answer = 0
    for i in range(n):
        for j in range(n):
            if computers[i][j] == 1 and i != j:
                answer += 1
                stack = []
                computers[i][j] = 0
                stack.append(j)
                while stack:
                    x = stack.pop()
                    for k in range(n):
                        if computers[x][k] == 1: 
                            if x != k:
                                computers[x][k] = 0
                                stack.append(k)
                            else:
                                computers[x][k] = 0

    for i in range(n):
        for j in range(n):
            if computers[i][j] == 1 and i == j:
                answer += 1
    
    return answer

# print(solution(3,[[1, 1, 0], [1, 1, 0], [0, 0, 1]]))


print(solution(3,[[1, 1, 0], [1, 1, 1], [0, 1, 1]]))