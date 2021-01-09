def solution(tickets):
    global answer
    answer = []
    K = len(tickets)
    recursive(tickets, "ICN", ["ICN"], K, 0, [0] * K)
    return answer


def recursive(tickets, now, lst, K, cnt, visited):
    if cnt == K:
        answer.append(lst)
        return

    for i in range(len(tickets)):
        if tickets[i][0] == now and visited[i] == 0:
            visited[i] = 1
            lst.append(tickets[i][1])
            recursive(tickets, tickets[i][1], lst, K, cnt + 1, visited)

    return




print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))
print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]))