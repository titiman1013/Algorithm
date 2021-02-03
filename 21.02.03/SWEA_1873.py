import sys; sys.stdin = open('1873.txt', 'r')

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

def search_pos():
    for i in range(H):
        for j in range(W):
            if arr[i][j] == '^' or arr[i][j] == 'v' or arr[i][j] == '<' or arr[i][j] == '>':
                return (i, j)


def activate(command, pos):
    if command == 'U':
        nx, ny = pos[0] + dx[0], pos[1] + dy[0]
        if 0 <= nx < H and 0 <= ny < W:
            if arr[nx][ny] == '.':
                arr[pos[0]][pos[1]] = '.'
                arr[nx][ny] = '^'
                pos = (nx, ny)
            else:
                arr[pos[0]][pos[1]] = '^'
        else:
            arr[pos[0]][pos[1]] = '^'
    elif command == 'D':
        nx, ny = pos[0] + dx[1], pos[1] + dy[1]
        if 0 <= nx < H and 0 <= ny < W:
            if arr[nx][ny] == '.':
                arr[pos[0]][pos[1]] = '.'
                arr[nx][ny] = 'v'
                pos = (nx, ny)
            else:
                arr[pos[0]][pos[1]] = 'v'
        else:
            arr[pos[0]][pos[1]] = 'v'
    elif command == 'L':
        nx, ny = pos[0] + dx[2], pos[1] + dy[2]
        if 0 <= nx < H and 0 <= ny < W:
            if arr[nx][ny] == '.':
                arr[pos[0]][pos[1]] = '.'
                arr[nx][ny] = '<'
                pos = (nx, ny)
            else:
                arr[pos[0]][pos[1]] = '<'
        else:
            arr[pos[0]][pos[1]] = '<'
    elif command == 'R':
        nx, ny = pos[0] + dx[3], pos[1] + dy[3]
        if 0 <= nx < H and 0 <= ny < W:
            if arr[nx][ny] == '.':
                arr[pos[0]][pos[1]] = '.'
                arr[nx][ny] = '>'
                pos = (nx, ny)
            else:
                arr[pos[0]][pos[1]] = '>'
        else:
            arr[pos[0]][pos[1]] = '>'
    elif command == 'S':
        if arr[pos[0]][pos[1]] == '^':
            nx, ny = pos[0], pos[1]
            while 0 <= nx < H and 0 <= ny < W:
                nx, ny = nx + dx[0], ny + dy[0]
                if 0 <= nx < H and 0 <= ny < W:
                    if arr[nx][ny] == '*':
                        arr[nx][ny] = '.'
                        break
                    elif arr[nx][ny] == '#':
                        break
        elif arr[pos[0]][pos[1]] == 'v':
            nx, ny = pos[0], pos[1]
            while 0 <= nx < H and 0 <= ny < W:
                nx, ny = nx + dx[1], ny + dy[1]
                if 0 <= nx < H and 0 <= ny < W:
                    if arr[nx][ny] == '*':
                        arr[nx][ny] = '.'
                        break
                    elif arr[nx][ny] == '#':
                        break
        elif arr[pos[0]][pos[1]] == '<':
            nx, ny = pos[0], pos[1]
            while 0 <= nx < H and 0 <= ny < W:
                nx, ny = nx + dx[2], ny + dy[2]
                if 0 <= nx < H and 0 <= ny < W:
                    if arr[nx][ny] == '*':
                        arr[nx][ny] = '.'
                        break
                    elif arr[nx][ny] == '#':
                        break
        elif arr[pos[0]][pos[1]] == '>':
            nx, ny = pos[0], pos[1]
            while 0 <= nx < H and 0 <= ny < W:
                nx, ny = nx + dx[3], ny + dy[3]
                if 0 <= nx < H and 0 <= ny < W:
                    if arr[nx][ny] == '*':
                        arr[nx][ny] = '.'
                        break
                    elif arr[nx][ny] == '#':
                        break
    return pos



for tc in range(1, int(input()) + 1):
    H, W = map(int, input().split())
    arr = [list(map(str, input())) for _ in range(H)]
    N = int(input())
    commands = input()

    pos = search_pos()
                
    for command in commands:
        pos = activate(command, pos)
    
    print(f'#{tc}', end=' ')
    for i in range(H):
        for j in range(W):
            print(arr[i][j], end='')
        print()