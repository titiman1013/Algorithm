def solution(progresses, speeds):
    answer = []

    N = len(progresses)
    days = [0] * N
    for i in range(N):
        if (100 - progresses[i]) % speeds[i]:
            days[i] = (100 - progresses[i]) // speeds[i] + 1
        else:
            days[i] = (100 - progresses[i]) // speeds[i]
    
    start = days[0]
    idx = 1
    cnt = 1
    while idx < N:
        if start >= days[idx]:
            cnt += 1
        else:
            start = days[idx]
            answer.append(cnt)
            cnt = 1
        idx += 1
        if idx == N:
            answer.append(cnt)

    return answer




print(solution([93, 30, 55], [1, 30, 5]))
print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))