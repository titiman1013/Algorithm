import sys; sys.stdin = open('2819.txt', 'r')

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

def create_num(num, stack):
    x, y = stack.pop()
    num += arr[x][y]
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < 4 and 0 <= ny < 4:
            if len(num) == 6:
                nums.add(num + arr[nx][ny])
            else:
                stack.append((nx, ny))
                create_num(num, stack)



for tc in range(1, int(input()) + 1):
    arr = list(list(map(str, input().split())) for _ in range(4))
    answer = 0

    nums = set()
    for i in range(4):
        for j in range(4):
            create_num('', [(i, j)])

    answer = len(nums)

    print(f'#{tc} {answer}')