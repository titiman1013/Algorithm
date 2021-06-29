import sys; sys.stdin = open('20058.txt', 'r')

# pypy

import sys


input = sys.stdin.readline
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

def fire_storm(spell):
    global arr

    tmp_arr = [[0] * 2 ** N for _ in range(2 ** N)]
    for start_x in range(0, 2 ** N, spell):
        for start_y in range(0, 2 ** N, spell):
            section = [[0] * spell for _ in range(spell)]
            for i in range(spell):
                for j in range(spell):
                    section[i][j] = arr[start_x + i][start_y + j]
            section = rotate(section)
            for i in range(spell):
                for j in range(spell):
                    tmp_arr[start_x + i][start_y + j] = section[i][j]
    arr = melt(tmp_arr)
    return


def rotate(section):
    return [list(elem) for elem in zip(*section[::-1])]


def melt(tmp_arr):
    result_arr = [[0] * (2 ** N) for _ in range(2 ** N)]
    for i in range(2 ** N):
        for j in range(2 ** N):
            if tmp_arr[i][j]:
                cnt = 0
                for k in range(4):
                    nx, ny = i + dx[k], j + dy[k]
                    if 0 <= nx < 2 ** N and 0 <= ny < 2 ** N:
                        if tmp_arr[nx][ny]:
                            cnt += 1
                result_arr[i][j] = tmp_arr[i][j] - 1 if cnt < 3 else tmp_arr[i][j]

    return result_arr


def sum_ice():
    total = 0
    for i in range(2 ** N):
        for j in range(2 ** N):
            if arr[i][j]:
                total += arr[i][j]
    
    return total


def block_length():
    visited = [[False] * (2 ** N) for _ in range(2 ** N)]
    max_length = 0
    for i in range(2 ** N):
        for j in range(2 ** N):
            if arr[i][j] and visited[i][j] == False:
                visited[i][j] = True
                length = 0
                stack = [(i, j)]
                while stack:
                    x, y = stack.pop()
                    length += 1
                    for k in range(4):
                        nx, ny = x + dx[k], y + dy[k]
                        if 0 <= nx < 2 ** N and 0 <= ny < 2 ** N:
                            if arr[nx][ny] and visited[nx][ny] == False:
                                visited[nx][ny] = True
                                stack.append((nx, ny))
                max_length = max(max_length, length)
    
    return max_length



for tc in range(1, int(input()) + 1):
    N, Q = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(2 ** N)]
    spells = list(map(int, input().split()))

    for spell in spells:
        fire_storm(2 ** spell)

    print(sum_ice())
    print(block_length())