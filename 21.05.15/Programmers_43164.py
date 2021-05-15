# reculsive error

# from collections import defaultdict

# def reculsive(depart, visited):
#     global answer
#     if len(visited) == N + 1:
#         if answer:
#             for i in range(N + 1):
#                 if visited[i] < answer[i]:
#                     answer = visited
#                     return
#             else:
#                 return
            
#         else:
#             answer = visited
#             return

#     for arrive in airports[depart]:
#         visited.append(arrive)
#         reculsive(arrive, visited)




# def solution(tickets):
#     global answer, airports, N
#     answer = []

#     N = len(tickets)
#     airports = defaultdict(list)
#     for depart, arrive in tickets:
#         airports[depart].append(arrive)

#     reculsive("ICN", ["ICN"])

#     return answer




#

from collections import defaultdict

def dfs(start, airports):
    global answer
    while airports[start]:
        end = airports[start].pop()
        dfs(end, airports)
    answer.append(start)


def solution(tickets):
    global answer
    answer = []

    airports = defaultdict(list)
    for depart, arrive in sorted(tickets, reverse=True):
        airports[depart].append(arrive)
    dfs("ICN", airports)

    return answer[::-1]




print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))
print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]))

# answer
# ["ICN", "JFK", "HND", "IAD"]
# ["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"]