from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

arr = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    ['*', 0, '#']
    ]

def solution(numbers, hand):
    answer = ''
    left_last_key = '*'
    right_last_key = '#'
    que = deque()
    for number in numbers:
        if number == 1 or number == 4 or number == 7:
            answer += 'L'
            left_last_key = number
        elif number == 3 or number == 6 or number == 9:
            answer += 'R'
            right_last_key = number
        elif number == 2 or number == 5 or number == 8 or number == 0:
            distance = [
                [0, 0, 0],
                [0, 0, 0],
                [0, 0, 0],
                [0, 0, 0]
                ]
            for i in range(len(arr)):
                for j in range(len(arr[i])):
                    if arr[i][j] == number:
                        que.append((i, j))
                        while que:
                            x, y = que.popleft()
                            for k in range(4):
                                nx = x + dx[k]
                                ny = y + dy[k]
                                if 0 <= nx < 4 and 0 <= ny < 3:
                                    if distance[nx][ny] == 0:
                                        if nx == i and ny == j:
                                            continue
                                        else:
                                            distance[nx][ny] = distance[x][y] + 1
                                            que.append((nx, ny))
                        # for z in distance:
                        #     print(z)
                        # print('')
                                    
            temp_left = 0
            temp_right = 0
            for i in range(len(arr)):
                for j in range(len(arr[i])):
                    if arr[i][j] == left_last_key:
                        temp_left = distance[i][j]
                    elif arr[i][j] == right_last_key:
                        temp_right = distance[i][j]
            if temp_left < temp_right:
                answer += 'L'
                left_last_key = number
            elif temp_right < temp_left:
                answer += 'R'
                right_last_key = number
            elif temp_left == temp_right:
                if hand == 'left':
                    answer += 'L'
                    left_last_key = number
                elif hand == 'right':
                    answer += 'R'
                    right_last_key = number
            
    return answer


print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"))
print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left"))
print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], 'right'))
print(solution([2, 0, 8, 5, 1, 7, 5, 1, 9, 8, 1, 9, 2], 'left'))