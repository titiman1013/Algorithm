import sys
sys.stdin = open("높은선반.txt", "r")


def search(cnt):
    global minimum
    if cnt == len(select):
        temp = 0
        for i in range(len(select)):
            if select[i] == True:
                temp += height[i]
        if temp >= B:
            if temp < minimum:
                minimum = temp
        return
    select[cnt] = True
    search(cnt+1)
    select[cnt] = False
    search(cnt+1)


T = int(input())
for t in range(T):
    N, B = map(int, input().split())
    height = list(map(int, input().split()))
    select = [False] * N
    minimum = sum(height) + 1
    search(0)

    print(f'#{t+1} {minimum-B}')