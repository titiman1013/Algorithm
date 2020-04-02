import sys; sys.stdin = open("pizza.txt", "r")

# # 시간초과
# for tc in range(1, int(input())+1):
#     N, M = map(int, input().split())
#     # N: 동시에 구울 수 있는 피자 개수
#     # M: 구워야할 피자 개수
#     arr = list(map(int, input().split()))
#     # C: 치즈양, //2 해서 0이되면 뺀다
#     # 입구는 하나

#     que = [arr[0]]
#     # res_list = []
#     num_list = [1]
#     a = 1
#     while a < M and len(que) != N:
#         que.append(arr[a])
#         a += 1
#         num_list.append(a)

#     while len(que) > 1:
#         for i in range(len(que)):
#             que[i] = que[i] // 2

#         # for i in range(len(que)):
#             if que[i] == 0:
#                 # res_list.append(que.pop(i))
#                 que.pop(i)
#                 num_list.pop(i)
#                 if len(num_list) == 1:
#                     break
#                 if a < M:
#                     que.insert(i, arr[a])
#                     a += 1
#                     num_list.insert(i, a)
#                 else:
#                     que.insert(i, 0)
#                     num_list.insert(i, 0)
#                     # print('check')

#         if len(num_list) != 1:
#             for i in range(len(que)-1, -1, -1):
#                 if que[i] == 0:
#                     que.pop(i)
#                     num_list.pop(i)

#         if len(que) == 1:
#             break

#     print(f'#{tc} {num_list[0]}')


# # 
# for tc in range(1, int(input())+1):
#     N, M = map(int, input().split())
#     arr = list(map(int, input().split()))

# # deque 사용
# import collections
# for tc in range(1,int(input())+1):
#     N,M = map(int,input().split())
#     arr = list(enumerate(list(map(int,input().split())),start=1))
#     q = collections.deque(arr[:N])
#     cnt = N
#     while q:
#         temp = q.popleft()
#         if temp[1]//2<=0:
#             if cnt<M:
#                 q.append(arr[cnt])
#                 cnt += 1
#         else:
#             q.append((temp[0],temp[1]//2))
#     print(f'#{tc} {temp[0]}')

# queue
T = int(input())
for tc in range(1, T+1):
    oven,pizza = map(int, input().split())
    cheeze = list(map(int, input().split()))
    queue = []
    for i in range(oven):
        queue.append([cheeze[i], i])
    idx = 0
    pizzaout=-1
    while len(queue)!=1:
        queue[0][0] //= 2
        if queue[0][0] == 0:
            if oven + idx < pizza:
                queue.pop(0)
                queue.append([cheeze[oven+idx], oven+idx])
                idx+=1
            elif oven+idx >= pizza:
                queue.pop(0)
        else:
            queue.append(queue.pop(0))
    print('#{} {}'.format(tc,queue[0][1]+1))