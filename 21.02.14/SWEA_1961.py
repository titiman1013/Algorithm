import sys; sys.stdin = open('1961.txt', 'r')

# 90도씩 회전시키는 함수
def rotate(temp_arr):
    return [list(elem) for elem in zip(*temp_arr[::-1])]



for tc in range(1, int(input()) + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    arr_90 = rotate(arr)
    arr_180 = rotate(rotate(arr))
    arr_270 = rotate(rotate(rotate(arr)))

    print(f'#{tc}')
    for i in range(N):
        temp_90, temp_180, temp_270 = '', '', ''
        for j in range(N):
            temp_90 += str(arr_90[i][j])
            temp_180 += str(arr_180[i][j])
            temp_270 += str(arr_270[i][j])
        print(temp_90, temp_180, temp_270)