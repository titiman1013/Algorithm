import sys; sys.stdin = open('common ancester.txt', 'r')
from collections import deque

# def ancester_search(num, ancester_list):
#     que = deque()
#     que.append(num)

#     while que:
#         number = que.popleft()
#         for i in range(len(sett)):
#             if sett[i][1] == number:
#                 ancester_list.append(sett[i][1])
#                 que.append(sett[i][1])



# for tc in range(1, int(input())+1):
#     V, E, num1, num2 = map(int, input().split())
#     # V: 정점수, E: 간선수, num1: 정점번호1, num2: 정점번호2
 
#     # arr = [[0] * V for _ in range(V)]
#     gansun = list(map(int, input().split()))
#     # for i in range(0, len(gansun), 2):
#     #     arr[gansun[i]-1][gansun[i+1]-1] = 1

#     sett = []
#     for i in range(0, len(gansun), 2):
#         sett.append((gansun[i], gansun[i+1]))
    
#     num1_ancester = []
#     num2_ancester = []
#     ancester_search(num1, num1_ancester)
#     ancester_search(num2, num2_ancester)

#     res_ancester = 0
#     stop_machine = 0
#     for i in range(len(num1_ancester)):
#         if stop_machine:
#             break
#         for j in range(len(num2_ancester)):
#             if num1_ancester[i] == num2_ancester[j]:
#                 res_ancester = num1_ancester
#                 stop_machine = 1
#                 break

#     res_subtree = 0
#     start = []
#     for i in range(len(sett)):
#         if sett[i][0] == res_ancester:



# 
def ancester_search(num, ancester_list):
    que = deque()
    que.append(num)

    while que:
        number = que.popleft()
        for i in range(len(sett)):
            if sett[i][1] == number:
                ancester_list.append(sett[i][1])
                que.append(sett[i][1])




for tc in range(1, int(input())+1):
    V, E, num1, num2 = map(int, input().split())
    # V: 정점수, E: 간선수, num1: 정점번호1, num2: 정점번호2
 
    arr = [[0] * V for _ in range(V)]
    gansun = list(map(int, input().split()))
    for i in range(0, len(gansun), 2):
        arr[gansun[i]-1][gansun[i+1]-1] = 1

    sett = []
    for i in range(0, len(gansun), 2):
        sett.append((gansun[i], gansun[i+1]))
    
    num1_ancester = []
    num2_ancester = []
    ancester_search(num1, num1_ancester)
    ancester_search(num2, num2_ancester)

    print('check_point')

    res_ancester = 0
    stop_machine = 0
    for i in range(len(num1_ancester)):
        if stop_machine:
            break
        for j in range(len(num2_ancester)):
            if num1_ancester[i] == num2_ancester[j]:
                res_ancester = num1_ancester
                stop_machine = 1
                break

    print(res_ancester)

    res_subtree = 0
