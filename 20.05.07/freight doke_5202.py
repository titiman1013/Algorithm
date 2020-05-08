import sys; sys.stdin = open('freight doke.txt', 'r')

for tc in range(1, int(input())+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # 시작시간, 종료시간

    arr = list(sorted(arr))
    
    work_list = []
    start = 0
    end = 0
    for i in range(len(arr)):
        if arr[i][0] >= end:
            work_list.append(arr[i])
            start, end = arr[i][0], arr[i][1]
        if work_list:
            if work_list[-1][1] - work_list[-1][0] > arr[i][1] - arr[i][0]:
                work_list.pop()
                work_list.append(arr[i])
                start, end = arr[i][0], arr[i][1]

    print(f'#{tc} {len(work_list)}')