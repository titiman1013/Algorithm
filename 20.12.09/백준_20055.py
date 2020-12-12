import sys; sys.stdin = open('text1.txt', 'r')

def robot_move(idx):
    for i in range(len(robot)):
        if arr[robot[i] + 1] != 0:
            robot[i] += 1
            arr[robot[i] + 1] -= 1
        if robot[i] > idx + 3:
            robot[i] = 'out'

    return
    

def robot_drop(robot_list, val):
    return [value for value in robot_list if value != val]


def finish_check():
    cnt = 0
    for i in range(N * 2):
        if arr[i] == 0:
            cnt += 1
    if cnt >= K:
        return 1
    else:
        print('cnt', cnt)''
        return 0



for tc in range(1, int(input()) + 1):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))
    
    res = 1
    start_point = 0
    finish = 0
    robot = []

    while finish == 0:
        # 벨트 한 칸 이동
        start_point -= 1
        # 벨트가 2N+1위치가 되면 1의 위치로 바꿔줌
        if start_point < -(N * 2):
            start_point = -1
        
        
        # 로봇 이동
        if len(robot) != 0:
            robot_move(start_point)
            robot = robot_drop(robot, 'out')

        # 로봇 올리기
        robot.append(start_point)
        arr[start_point] -= 1
            
        # 전체 내구도 체크
        finish = finish_check()
        if finish == 1:
            break

        res += 1
        print(arr)
        print('---------')

    print(f'#{tc} {res}')