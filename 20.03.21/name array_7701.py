import sys; sys.stdin = open('name array', 'r')

T = int(input())
ans = []
for tc in range(T):
    N = int(input())
    myungbu = [set() for _ in range(50)]
    # print(myungbu)
    for i in range(N):
        name = input()
        myungbu[len(name)-1].add(name)
    # print(myungbu)
    res = []
    for j in myungbu:
        if j:
            n_j = list(j)
            res += sorted(n_j)
    print(f'#{tc+1}')
    for k in res:
        print(k)
 