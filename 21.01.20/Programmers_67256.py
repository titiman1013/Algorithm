def solution(numbers, hand):
    answer = ''

    arr = [(3, 1), (0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2), (3, 0), (-1, -1), (3, 2)]
    pos_left, pos_right = arr[10], arr[12]
    for i in range(len(numbers)):
        if numbers[i] in [1, 4, 7]:
            answer += 'L'
            pos_left = arr[numbers[i]]
        elif numbers[i] in [3, 6, 9]:
            answer += 'R'
            pos_right = arr[numbers[i]]
        else:
            temp, pos_left, pos_right = dis_calc(arr[numbers[i]], pos_left, pos_right, hand)
            answer += temp

    return answer


def dis_calc(target, pos_left, pos_right, hand):
    if target == pos_left:
        return 'L', target, pos_right
    elif target == pos_right:
        return 'R', pos_left, target

    # dis_l = (abs(pos_left[0] - target[0]) ** 2 + abs(pos_left[1] - target[1]) ** 2) ** 0.5
    # dis_r = (abs(pos_right[0] - target[0]) ** 2 + abs(pos_right[1] - target[1]) ** 2) ** 0.5
    dis_l = abs(pos_left[0] - target[0]) + abs(pos_left[1] - target[1])
    dis_r = abs(pos_right[0] - target[0]) + abs(pos_right[1] - target[1])

    if dis_l < dis_r:
        return 'L', target, pos_right
    elif dis_l > dis_r:
        return 'R', pos_left, target
    elif dis_l == dis_r:
        if hand == 'left':
            return 'L', target, pos_right
        else:
            return 'R', pos_left, target







print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"))
print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left"))
print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], "right"))
print(solution([2, 0, 5, 8, 2, 0, 8, 5, 2, 0, 5, 8], 'left'))

# answer
# "LRLLLRLLRRL"
# "LRLLRRLLLRR"
# "LLRLLRLLRL"