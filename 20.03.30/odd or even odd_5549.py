import sys; sys.stdin = open("odd or even odd.txt", "r")

for tc in range(1, int(input())+1):
    N = int(input())
    if N % 2 == 1:
        print(f'#{tc} Odd')
    else: print(f'#{tc} Even')