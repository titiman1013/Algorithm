import sys; sys.stdin = open('hanaroad.txt', 'r')

def search(cnt, _sum, linked_island):
    global res
    if cnt == N:
        



for tc in range(1, int(input())+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(2)]
    E = float(input())
    # L: ((x2-x1)^2 + (y2-y1)^2)**1/2
    # E * L^2

    linked_length = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if i != j:
                linked_length[i][j] = int(abs(((arr[0][j]-arr[0][i])**2 + (arr[1][j]-arr[1][i])**2) * E))
    
    linked_island = [0] * N
    res_list = []
    search()