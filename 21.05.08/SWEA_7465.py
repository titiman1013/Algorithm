import sys; sys.stdin = open('7465.txt', 'r')

from collections import defaultdict

def dfs(start, stack):
    num = stack.pop()
    check[num] = start
    for link_node in people[num]:
        if check[link_node] == 0:
            stack.append(link_node)
            dfs(start, stack)



for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    arr = list(list(map(int, input().split())) for _ in range(M))
    answer = 0

    people = defaultdict(list)
    check = [0] * (N + 1) 
    for i in range(M):
        people[arr[i][0]].append(arr[i][1])
        people[arr[i][1]].append(arr[i][0])
    
    for i in range(1, N + 1):
        if check[i] == 0:
            dfs(i, [i])
            answer += 1
    
    print(f'#{tc} {answer}')