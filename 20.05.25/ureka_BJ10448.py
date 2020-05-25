import sys; sys.stdin = open('ureka.txt', 'r')

def check(_sum, cnt, array):
    global res
    if res:
        return

    if cnt == 3:
        if _sum == N:
            res = 1
        return

    check(_sum+triangle_list[array], cnt+1, array)
    if array + 1 < len(triangle_list):
        check(_sum, cnt, array+1)


triangle_list = []
a = 0
for i in range(1000):
    a += i
    if a:
        triangle_list.append(a)
    if a > 1000:
        break
    

for tc in range(1, int(input())+1):
    N = int(input())
    res = 0
    check(0, 0, 0)

    print(f'#{tc} {res}')