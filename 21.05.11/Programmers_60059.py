def rotate(key):
    return [list(elem) for elem in zip(*key[::-1])]


def create_key_points(key, M):
    points = []
    for i in range(M):
        for j in range(M):
            if key[i][j] == 1:
                points.append((i, j))
    return points


def create_lock_points(lock, N):
    points = []
    for i in range(N):
        for j in range(N):
            if lock[i][j] == 0:
                points.append((i, j))
    return points


def open_lock(key, lock, N, lock_point, key_points, start):
    arr = [[0] * 61 for _ in range(61)]
    for i in range(N):
        for j in range(N):
            if lock[i][j] == 1:
                arr[i + 20][j + 20] += 1

    arr[20 + lock_point[0]][20 + lock_point[1]] += 1

    for x, y in key_points:
        arr[20 + lock_point[0] + (x - start[0])][20 + lock_point[1] + (y - start[1])] += 1
    
    return arr


def check(check_arr, N):
    for i in range(20, 20 + N):
        for j in range(20, 20 + N):
            if check_arr[i][j] != 1:
                return False
    return True


def solution(key, lock):
    answer = False

    N, M = len(lock), len(key)

    for _ in range(4):
        key = rotate(key)
        key_points, lock_points = create_key_points(key, M), create_lock_points(lock, N)
        if lock_points:
            for lock_point in lock_points:
                for i in range(len(key_points)):
                    start = key_points.pop(0)
                    union = open_lock(key, lock, N, lock_point, key_points, start)
                    if check(union, N):
                        return True
                    key_points.append(start)
        else:
            return True
            
    return answer




print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))

# answer
# true