#

# def reculsive(answer, n, arr, linked, total_cost):
#     if len(linked) == n - 1:
#         if total_cost < answer:
#             answer = total_cost
#         return

    


# def solution(n, costs):
#     answer = 0

#     arr = [[0] * n for _ in range(n)]
#     for i, j, cost in costs:
#         arr[i][j] = cost
#         arr[j][i] = cost

#     linked = [False] * n
#     total_cost = 0

#     return answer



# kruskal argorithm

def solution(n, costs):
    answer = 0

    # 낮은 cost순으로 정렬
    costs.sort(key=lambda x: x[2])
    routes = set([costs[0][0]])
    while len(routes) < n:
        # 낮은 cost순으로 sort된 list이기 때문에 비용비교는 고려할 필요가 없다
        for idx, cost in enumerate(costs):
            # 이미 연결되었을 경우
            if cost[0] in routes and cost[1] in routes:
                continue
            # 현재 연결된 길과 연결이 가능할 경우
            if cost[0] in routes or cost[1] in routes:
                # 고립 상태의 길을 연결
                routes.update([cost[0], cost[1]])
                answer += cost[2]
                # 연결시킨 길을 costs에서 삭제
                del costs[idx]
                # 탐색 다시 시작
                break

    return answer
 




print(solution(4, [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]))

# answer
# 4