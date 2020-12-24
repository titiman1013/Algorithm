import sys; sys.stdin = open('text1.txt', 'r')
# from collections import deque

# def check(total, start, end, up, down):
#     if start == end:
#         return 0

#     q = deque()
#     q.append(start)
    
#     while q:
#         x = q.popleft()
#         for k in [up, -down]:
#             nx = x + k
#             if 0 < nx <= total and arr[nx] == 0:
#                 arr[nx] = arr[x] + 1
#                 if nx == end:
#                     return arr[nx]
#                 else:
#                     q.append(nx)
#     return 'use the stairs'


# for tc in range(1, int(input()) + 1):
#     # F: 전체 층, S: 현재 층, G: 스타트링크 위치(Target), U: Up Btn, D: Down Btn
#     F, S, G, U, D = map(int, input().split())
    
#     arr = [0] * (F + 1)
#     res = check(F, S, G, U, D)
#     print(res)


from collections import deque

def check(total, start, end, up, down):
    if start == end:
        return 0

    q = deque()
    q.append(start)
    
    while q:
        x = q.popleft()
        for k in [up, -down]:
            nx = x + k
            if 0 < nx <= total and arr[nx] == -1:
                arr[nx] = arr[x] + 1
                q.append(nx)

    if arr[end] == -1:
        return 'use the stairs'
    else:
        return arr[end]


for tc in range(1, int(input()) + 1):
    # F: 전체 층, S: 현재 층, G: 스타트링크 위치(Target), U: Up Btn, D: Down Btn
    F, S, G, U, D = map(int, input().split())
    
    arr = [-1] * (F + 1)
    arr[S] = 0
    res = check(F, S, G, U, D)
    print(res)