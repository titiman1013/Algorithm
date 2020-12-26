import sys; sys.stdin = open('text1.txt', 'r')


# dir_list = ['D', 'L', 'U', 'R']


def sort_arr():
    temp_list = [(0, 0)]
    x, y = 0, 0
    go = 0
    for i in range(len(arr)):
        if arr[i] == 'L':
            go -= 1
            if go == -5:
                go = -1
        elif arr[i] == 'R':
            go += 1
            if go == 4:
                go = 0
        elif arr[i] == 'F':
            if go == 0 or go == -4:
                x += 1
            elif go == 1 or go == -3:
                y -= 1
            elif go == 2 or go == -2:
                x -= 1
            elif go == 3 or go == -1:
                y += 1
            temp_list.append((x, y))
    # print(temp_list)
    return sorted(temp_list)


def calc_length():
    min_hor, min_ver = 51, 51
    max_hor, max_ver = -51, -51
    for i in range(len(map_component)):
        if map_component[i][0] < min_ver:
            min_ver = map_component[i][0]
        elif map_component[i][0] > max_ver:
            max_ver = map_component[i][0]
        
        if map_component[i][1] < min_hor:
            min_hor = map_component[i][1]
        elif map_component[i][1] > max_hor:
            max_hor = map_component[i][1]
    
    return max_ver - min_ver + 1, max_hor - min_hor + 1, min_ver, min_hor


def create_map(height, width, min_ver, min_hor):
    arr = [[-1] * width for _ in range(height)]
    
    for i in map_component:
        x, y = i[0] + min_ver, i[1] + min_hor
        arr[x][y] = '.'
    
    for i in range(height):
        for j in range(width):
            if arr[i][j] == -1:
                arr[i][j] = '#'
    return arr


# 시작은 남쪽방향을 보고 서있다
# .은 이동할 수 있는 칸, #은 벽
N = int(input())
arr = input()
map_component = sort_arr()
# print(map_component)
height, width, min_ver, min_hor = calc_length()
# print(height, width)
map_list = create_map(height, width, min_ver, min_hor)

for i in range(height):
    for j in range(width):
        print(map_list[i][j], end='')
    print()