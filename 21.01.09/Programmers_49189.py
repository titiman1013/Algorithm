from collections import deque

def solution(n, edge):
    arr = [[0] * (n + 1) for _ in range(n + 1)]
    for x, y in edge:
        arr[x][y] = 1
        arr[y][x] = 1
    
    visited = [0] * (n + 1)
    d = deque()
    d.append(1)
    visited[1] = 1
    while d:
        x = d.popleft()
        for k in range(1, n + 1):
            if arr[x][k] and visited[k] == 0:
                visited[k] = visited[x] + 1
                d.append(k)
    
    max_lst = []
    max_len = max(visited)
    for i in range(1, n + 1):
        if visited[i] == max_len:
            max_lst.append(i)
    
    answer = len(max_lst)

    return answer




print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))