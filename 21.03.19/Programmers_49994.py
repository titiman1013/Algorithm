dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

def arr_create():
    arr = [[0] * 11 for _ in range(11)]
    return arr


def move(visited, arr, x, y, k):
    nx, ny = x + dx[k], y + dy[k]
    if 0 <= nx < 11 and 0 <= ny < 11:
        visited = first_check(visited, x, y, nx, ny)
        return visited, arr, [nx, ny]
    return visited, arr, [x, y]


def first_check(visited, x, y, nx, ny):
    visited.add(tuple(sorted([(x, y), (nx, ny)])))
    return visited


def solution(dirs):
    answer = 0

    arr = arr_create()
    pos = [5, 5]
    visited = set()
    for dir in dirs:
        if dir == 'U':
            visited, arr, pos = move(visited, arr, *pos, 0)
        elif dir == 'D':
            visited, arr, pos = move(visited, arr, *pos, 1)
        elif dir == 'L':
            visited, arr, pos = move(visited, arr, *pos, 2)
        else:
            visited, arr, pos = move(visited, arr, *pos, 3)

    answer = len(visited)

    return answer




print(solution("ULURRDLLU"))
print(solution("LULLLLLLU"))

# answer
# 7
# 7