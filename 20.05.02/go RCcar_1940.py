import sys; sys.stdin = open('go RCcar.txt', 'r')

for tc in range(1, int(input())+1):
    n = int(input())
    ans = 0
    speed = 0
    for _ in range(n):
        commands = list(map(int, input().split()))
        if len(commands) == 1:
            ans += speed
        else:
            if commands[0] == 1:
                speed += commands[1]
                ans += speed
            else:
                if not ans: continue
                speed -= commands[1]
                ans += speed
    print("#{} {}".format(tc, ans))