import sys; sys.stdin = open('1347.txt', 'r')


dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]

command_length = int(input())
commands = input()

dir = 2
pos = [0, 0]
x_list = [0]
y_list = [0]
for command in commands:
    if command == 'L':
        dir = (dir - 1) % 4
    elif command == 'R':
        dir = (dir + 1) % 4
    elif command == 'F':
        x, y = pos
        nx, ny = x + dx[dir], y + dy[dir]
        x_list.append(nx)
        y_list.append(ny)
        pos = [nx, ny]

max_x, min_x, max_y, min_y = max(x_list), min(x_list), max(y_list), min(y_list)
N, M = max_x - min_x + 1, max_y - min_y + 1
start_x, start_y = abs(min_x), abs(min_y)
maze = [['#'] * M for _ in range(N)]
for x, y in zip(x_list, y_list):
    maze[start_x + x][start_y + y] = '.'

for line in maze:
    print("".join(line))