import sys; sys.stdin = open("cube root.txt", "r")

for tc in range(1, int(input())+1):
    N = int(input())
    for i in range(int(N**(1/3))+2):
        if i ** 3 == N:
            print(f'#{tc} {i}')
            break     
    else: print(f'#{tc} {-1}')