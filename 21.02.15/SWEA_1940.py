import sys; sys.stdin = open('1940.txt', 'r')

for tc in range(1, int(input()) + 1):
    N = int(input())
    commands = [list(map(int, input().split())) for _ in range(N)]

    answer = 0
    vel = 0
    for command in commands:
        if command[0] == 0:
            if vel:
                answer += vel
        elif command[0] == 1:
            vel += command[1]
            answer += vel
        elif command[0] == 2:
            vel -= command[1]
            if vel < 0:
                vel = 0
                continue
            answer += vel
    
    print(f'#{tc} {answer}')