import math

def solution(a):
    answer = 0

    # 기본적으로 풍선은 큰 것을 터뜨린다
    # 앞, 뒤는 무조건 남길 수 있고, 
    # 가운데 위치한 풍선은 자신을 기준으로 좌리스트와 우리스트의 최소값보다 하나이상 작으면 남길 수 있다
    left, right = math.inf, math.inf
    # 양 끝단부터 최소값을 비교해서 결과값을 리스트에 저장
    arr = [[0] * len(a) for _ in range(2)]

    for i in range(len(a)):
        # 좌를 기준으로 작은 풍선을 남긴다
        if left > a[i]:
            left = a[i]
        arr[0][i] = left

        # 우를 기준으로 큰 풍선을 남긴다
        if right > a[-i - 1]:
            right = a[-i - 1]
        arr[1][-i - 1] = right

    # 최소값이 저장된 리스트를 기반으로 남길 수 있는지 확인
    for i in range(len(a)):
        if a[i] <= arr[0][i] or a[i] <= arr[1][i]:
            answer += 1

    return answer




print(solution([9,-1,-5]))
print(solution([-16,27,65,-2,58,-92,-71,-68,-61,-33]))

# answer
# 3
# 6