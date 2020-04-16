import sys; sys.stdin = open("subtree.txt", "r")

for tc in range(1, int(input())+1):
    E, N = map(int, input().split())
    arr = list(map(int, input().split()))
    # print(arr)
    tree = [[] for _ in range(E+2)]
    # print(tree)
    for i in range(E):
        tree[arr[i*2]].append(arr[i*2+1])
        # print(tree)
    res = 1
    stack = [N]
    while stack:
        x = stack.pop()
        for i in range(len(tree[x])):
            stack.append(tree[x][i])
            res += 1


    print(f'#{tc} {res}')