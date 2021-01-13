from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0

    bridge = deque([0] * bridge_length)
    d = deque(truck_weights)
    now_w = 0
    while d:
        now_w -= bridge.pop()
        if now_w + d[0] <= weight:
            truck = d.popleft()
            now_w += truck
            bridge.appendleft(truck)
        else:
            bridge.appendleft(0)
        answer += 1

    answer += bridge_length



    return answer




print(solution(2, 10, [7, 4, 5, 6]))
print(solution(100, 100, [10]))
print(solution(100, 100, [10,10,10,10,10,10,10,10,10,10]))