def go(arr, dir, end_point, num, pos):
    x, y = pos
    for i in range(end_point):
        if dir == 0:
            y += 1
        elif dir == 1:
            x, y = x - 1, y - 1
        else:
            x += 1
        arr[x][y] = num
        num += 1
    return arr, dir, end_point, num, [x, y]


def solution(n):
    answer = []

    if n == 1:
        return [1]

    arr = [[0] * i for i in range(1, n + 1)]
    # dir = ['right', 'up', 'down']
    dir = 0
    end_point = n
    num = 1
    pos = [0, 0]
    for i in range(end_point):
        arr[i][0] = num
        num += 1
        pos = [i, 0]
    end_point -= 1
    
    for i in range(n - 1):
        arr, dir, end_point, num, pos = go(arr, dir, end_point, num, pos)
        dir += 1
        if dir == 3: 
            dir = 0
        end_point -= 1
    
    for i in range(n):
        answer.extend(arr[i])

    return answer




print(solution(4))
print(solution(5))
print(solution(6))

# answer
# [1,2,9,3,10,8,4,5,6,7]
# [1,2,12,3,13,11,4,14,15,10,5,6,7,8,9]
# [1,2,15,3,16,14,4,17,21,13,5,18,19,20,12,6,7,8,9,10,11]