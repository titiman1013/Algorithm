import sys; sys.stdin = open("Node sum.txt", "r")

for tc in range(1, int(input())+1):
    N, M, L = map(int, input().split())
    tree = [0 for _ in range(N+1)]
    for i in range(M):
        num, value = map(int, input().split())
        tree[num] = value
    
    # for i in range(len(tree)):
        # if tree[i] == 0:
        #     if i * 2 + 1 <= N:
        #         tree[i] = tree[i*2] + tree[i*2+1]
    for i in range(len(tree)-1, -1, -1):
        tree[i//2] += tree[i]
    
    print(f'#{tc} {tree[L]}')



# # 1
# for tc in range(1, int(input())+1):
#     N, M, L = map(int, input().split())
#     TREE = [0 for _ in range(N+1)]
#     for _ in range(M):
#         idx, value = map(int, input().split())
#         TREE[idx] = value

#     n = N
#     while n > 1:
#         TREE[n//2] += TREE[n]
#         n -= 1


#     print(f'#{tc} {TREE[L]}')



# # 2
# def post_order(n):
#     if n > N:
#         return 0
#     if TREE[n] > 0:
#         return TREE[n]
#     a = post_order(n*2)
#     b = post_order(n*2+1)
#     TREE[n] = a + b
#     return a + b



# for tc in range(1, int(input())+1):
#     N, M, L = map(int, input().split())
#     TREE = [0 for _ in range(N+1)]
#     for _ in range(M):
#         idx, value = map(int, input().split())
#         TREE[idx] = value

#     post_order(1)

#     print(f'#{tc} {TREE[L]}')