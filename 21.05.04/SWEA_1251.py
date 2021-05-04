import sys; sys.stdin = open('1251.txt', 'r')

import heapq

for tc in range(1, int(input()) + 1):
    N = int(input())
    Xs = list(map(int, input().split()))
    Ys = list(map(int, input().split()))
    E = float(input())
    
    # round(n) => 정수

    # adjacency list
    adj = {i: [] for i in range(N)}
    for s in range(N):
        for e in range(N):
            if s != e:
                adj[s].append([e, (Xs[s] - Xs[e]) ** 2 + (Ys[s] - Ys[e]) ** 2])

    visited = [0] * N
    # minimum weight(cost)
    mc = [float('inf')] * N
    edge_list = []

    # start index = 0
    mc[0] = 0
    res = 0
    heapq.heappush(edge_list, (0, 0))
    while edge_list:
        minimum_cost, node1 = heapq.heappop(edge_list)
        if visited[node1]: continue
        else:
            visited[node1] = True
            res += minimum_cost
            for node2, cost in adj[node1]:
                # 방문한적이 없고 해당 정점과 연결된 간선의 최소비용을 찾았을 경우
                if visited[node2] == 0 and cost < mc[node2]:
                    mc[node2] = cost
                    heapq.heappush(edge_list, (cost, node2))

    answer = round(res * E)

    print(f'#{tc} {answer}')