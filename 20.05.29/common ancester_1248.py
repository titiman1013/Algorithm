import sys; sys.stdin = open('common ancester.txt', 'r')
from collections import deque

def ancester_search(num):
    que = deque()
    que.append(num)

    while que:
        number = que.popleft()
        for i in range(len(sett)):
            if sett[i][1] == number:
                if sett[i][1] in num_ancester:
                    res_ancester = sett[i][1]
                    return
                else:
                    num_ancester.append(sett[i][1])
                    que.append(sett[i][1])



for tc in range(1, int(input())+1):
    V, E, num1, num2 = map(int, input().split())
    # V: 정점수, E: 간선수, num1: 정점번호1, num2: 정점번호2
 
    # arr = [[0] * V for _ in range(V)]
    gansun = list(map(int, input().split()))
    # for i in range(0, len(gansun), 2):
    #     arr[gansun[i]-1][gansun[i+1]-1] = 1

    sett = []
    for i in range(0, len(gansun), 2):
        sett.append((gansun[i], gansun[i+1]))
    
    num_ancester = []
    ancester_search(num1)
    ancester_search(num2)