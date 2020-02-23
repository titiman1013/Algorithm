import sys
sys.stdin = open("그래프경로.txt" , "r")

T = int(input())
for t in range(T):
    V, E = map(int, input().split())
    visit = [] # 방문한곳
    neighbor = [] # 이동할수있는 인접장소
    arr = [] 
    current = 0

    for i in range(E):
        arr.append(list(map(int, input().split())))

    