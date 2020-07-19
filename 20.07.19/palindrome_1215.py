import sys; sys.stdin = open('palindrome.txt', 'r')

for tc in range(1, 11):
    N = int(input())
    arr = [input() for _ in range(8)]

    res = 0
    for i in range(8-N+1):
        for j in range(8-N+1):
            horizontal = 0
            hor_str = ''
            vertical = 0
            ver_str = ''
            for p in range(N//2):
                if arr[i][j+p] == arr[i][j+N-1-p]:
                    horizontal += 1
                    hor_str += arr[i][j+p]
                else: break
            for q in range(N//2):
                if arr[j+q][i] == arr[j+N-1-q][i]:
                    vertical += 1
                    ver_str += arr[j+q][i]
                else: break
            if horizontal == N // 2 or vertical == N // 2:
                res += 1
                print('hor:', hor_str, 'ver:', ver_str)

    print(f'#{tc} {res}')