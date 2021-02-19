from collections import Counter

# too much memory

def solution(N, stages):
    answer = []

    c_stages = Counter(stages)
    # stage지나간 사람, stage에서 멈춘 사람
    persons = [[0, 0] for _ in range(N+1)]
    for stay, cnt in c_stages.items():
        for stage in range(1, N + 1):
            if stay >= stage:
                if stay > N:
                    persons[stage][0] += cnt
                elif c_stages[stage]:
                    persons[stage][0] += cnt
        if stay <= N:
            persons[stay][1] += cnt
      
    failures = [0] * (N+1)
    for idx, person in enumerate(persons):
        if person[0] == 0 or person[1] == 0:
            failures[idx] = 0
        else:
            failures[idx] = person[1]/person[0]
    
    # failures.sort(reverse=True)
    print(failures)

    while failures:
        top = 0
        stage_num = 0
        for idx, failure in enumerate(failures):
            if failure > top:
                top = failure
                stage_num = idx

    return answer




# answer
# [3,4,2,1,5]
# [4,1,2,3]