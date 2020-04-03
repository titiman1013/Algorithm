import sys; sys.stdin = open("node distance.txt", "r")

for tc in range(1, int(input())+1):
    V, E = map(int, input().split())
    # V가 노드개수 E가 간선개수
    arrs = [list(map(int, input().split())) for _ in range(E)]
    S, G = map(int, input().split())
    # S는 출발점 G는 도착점

    # 각 node마다 갈 수 있는 곳을 gansun에 저장
    gansun = [[] for _ in range(V+1)]   # index맞춰주기 위해 +1
    for arr in arrs:
        gansun[arr[0]].append(arr[1])
        gansun[arr[1]].append(arr[0])

    # 출발점을 stack에 넣고 뽑아가며 뽑은 node가 갈 수 있는 node 판별
    dis = [0] * (V+1)
    visit = [S]
    stack = [S]
    while stack:
        cl = stack.pop(0)
        if cl == G: break
        for node in gansun[cl]:
            if node not in visit:
                stack.append(node)
                visit.append(node)
                dis[node] = dis[cl] + 1

    print(f'#{tc} {dis[G]}')