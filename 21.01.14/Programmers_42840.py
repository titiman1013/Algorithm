def solution(answers):
    answer = []

    A = [1, 2, 3, 4, 5]
    B = [2, 1, 2, 3, 2, 4, 2, 5]
    C = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    cnts = [0] * 3
    for i in range(len(answers)):
        if answers[i] == A[i % 5]:
            cnts[0] += 1
        if answers[i] == B[i % 8]:
            cnts[1] += 1
        if answers[i] == C[i % 10]:
            cnts[2] += 1
    
    for i in range(len(cnts)):
        if cnts[i] == max(cnts):
            answer.append(i + 1)

    return answer




print(solution([1,2,3,4,5]))
print(solution([1,3,2,4,2]))

# answer
# [1]
# [1, 2, 3]