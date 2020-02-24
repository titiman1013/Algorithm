N, M = list(map(int, input().split()))
arr = [list(map(int, input().split())) for i in range(N)]

clone = []
for i in range(N):
    for j in range(M):
        clone.append([])

for i in range(N):
    for j in range(M):
        