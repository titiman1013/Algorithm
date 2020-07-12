import sys; sys.stdin = open('pascal triangle.txt', 'r')

for tc in range(1, int(input())+1):
    N = int(input())

    print(f'#{tc}')

    start = [0, 1, 0]
    for i in range(N):
        lis = []
        if i == 0:
            print(1)
        else:
            for j in range(len(start) - 1):
                lis.append(start[j] + start[j+1])
            for li in lis:
                print(li, end=' ')
            print('')
            lis.append(0)
            lis.insert(0, 0)
            start = lis[:]