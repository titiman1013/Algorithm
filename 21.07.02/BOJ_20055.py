import sys; sys.stdin = open('20055.txt', 'r')

import sys
from collections import deque


input = sys.stdin.readline

def move_conveyor():
    down_conveyor.append(up_conveyor.pop())
    up_conveyor.appendleft(down_conveyor.popleft())
    for i in range(len(robots)):
        robots[i] += 1
        if robots[i] == N - 1:
            robots[i] = -1
    while robots.count(-1):
        robots.remove(-1)
    return


def move_robot():
    for robot in robots[::-1]:
        if up_conveyor[robot + 1] and robot + 1 not in robots:
            up_conveyor[robot + 1] -= 1
            if robot + 1 == N - 1:
                robots[robots.index(robot)] = -1
            else:
                robots[robots.index(robot)] += 1
    while robots.count(-1):
        robots.remove(-1)
    return


def put_robot():
    global robots

    if up_conveyor[0] and (not(robots) or robots[0] != 0):
        up_conveyor[0] -= 1
        robots = [0] + robots
    return



for tc in range(1, int(input()) + 1):
    N, K = map(int, input().split())
    durability = list(map(int, input().split()))

    up_conveyor = deque(durability[:N])
    down_conveyor = deque(durability[N:][::-1])
    robots = []

    answer = 0
    zero_cnt = 0
    while zero_cnt < K:
        answer += 1
        move_conveyor()
        move_robot()
        put_robot()
        zero_cnt = up_conveyor.count(0) + down_conveyor.count(0)

    print(answer)