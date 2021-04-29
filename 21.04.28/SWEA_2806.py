import sys; sys.stdin = open('2806.txt', 'r')

# array, row, column 
def backtrack(arr, idx, pos):
    global answer, N

    if idx == N:
        answer += 1
        return
    
    for j in range(N):
        for up in range(idx - 1, -1, -1):
            if arr[up] == j: continue
            elif abs(arr[up] - j) == abs(up - idx): continue
            else:
                arr[idx] = j
                backtrack(arr, idx + 1, 0)



for tc in range(1, int(input()) + 1):
    N = int(input())
    answer = 0

    arr = list(-1 for _ in range(N))
    for j in range(N):
        arr[0] = j
        backtrack(arr, 1, j)

    print(f'#{tc} {answer}')