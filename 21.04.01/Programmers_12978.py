from collections import deque

def solution(N, road, K):
    answer = 0

    nodes = {}
    for v1, v2, dis in road:
        nodes[v1] = nodes.get(v1, []) + [(v2, dis)]
        nodes[v2] = nodes.get(v2, []) + [(v1, dis)]

    distance = {i:float('inf') if i != 1 else 0 for i in range(1, N + 1)}

    # 1번 노드와의 거리 저장
    deq = deque([1])
    while deq:
        current_node = deq.popleft()
        for next_node, dis in nodes[current_node]:
            if distance[next_node] > distance[current_node] + dis:
                distance[next_node] = distance[current_node] + dis
                deq.append(next_node)

    answer = len([True for val in distance.values() if val <= K])

    return answer





print(solution(5, [[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]], 3))
print(solution(6, [[1,2,1],[1,3,2],[2,3,2],[3,4,3],[3,5,2],[3,5,3],[5,6,1]], 4))

# answer
# 4
# 4