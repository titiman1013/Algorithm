# too much memory

# from collections import Counter

# def solution(N, stages):
#     answer = []

#     c_stages = Counter(stages)
#     # stage지나간 사람, stage에서 멈춘 사람
#     persons = [[0, 0] for _ in range(N+1)]
#     for stay, cnt in c_stages.items():
#         for stage in range(1, N + 1):
#             if stay >= stage:
#                 if stay > N:
#                     persons[stage][0] += cnt
#                 elif c_stages[stage]:
#                     persons[stage][0] += cnt
#         if stay <= N:
#             persons[stay][1] += cnt
      
#     failures = [0] * (N+1)
#     for idx, person in enumerate(persons):
#         if person[0] == 0 or person[1] == 0:
#             failures[idx] = 0
#         else:
#             failures[idx] = person[1]/person[0]
    
#     # failures.sort(reverse=True)
#     print(failures)

#     while failures:
#         top = 0
#         stage_num = 0
#         for idx, failure in enumerate(failures):
#             if failure > top:
#                 top = failure
#                 stage_num = idx

#     return answer


#

from collections import Counter

def solution(N, stages):
    fail = {}
    clear = len(stages)
    cnts = Counter(stages)
    for i in range(1, N+1):
        if clear != 0:
            cnt = cnts.get(i)
            if cnt == None:
                fail[i] = 0
            else:
                fail[i] = cnt / clear
                clear -= cnt
        else:
            fail[i] = 0
            
    return sorted(fail, key=lambda x : fail[x], reverse=True)




# answer
# [3,4,2,1,5]
# [4,1,2,3]