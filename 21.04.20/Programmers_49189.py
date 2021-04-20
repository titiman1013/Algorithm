#

from collections import deque

def solution(n, vertex):
    answer = 0

    graph = dict()
    for node1, node2 in vertex:
        graph.setdefault(node1, []).append(node2)
        graph.setdefault(node2, []).append(node1)
    
    # node number, depth
    deq = deque([[1, 0]])
    # 거리 및 방문 여부
    visited = [-1] * (n + 1)
    while deq:
        n, depth = deq.popleft()
        visited[n] = depth
        for i in graph[n]:
            if visited[i] == -1:
                visited[i] = 0
                deq.append([i, depth + 1])
        depth += 1
    
    answer = visited.count(max(visited))

    return answer




print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))

# answer
# 3