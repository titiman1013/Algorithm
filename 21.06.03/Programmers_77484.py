def solution(lottos, win_nums):
    answer = []

    win_a_lottery = {
        0: 6,
        1: 6,
        2: 5,
        3: 4,
        4: 3,
        5: 2,
        6: 1,
    }

    max_num = 0
    min_num = 0

    for lotto in lottos:
        if lotto in win_nums:
            min_num += 1
        elif lotto == 0:
            max_num += 1

    answer = [win_a_lottery.get(min_num + max_num), win_a_lottery.get(min_num)]

    return answer




print(solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19]))
print(solution([0, 0, 0, 0, 0, 0], [38, 19, 20, 40, 15, 25]))
print(solution([45, 4, 35, 20, 3, 9], [20, 9, 3, 45, 4, 35]))

# answer
# [3, 5]
# [1, 6]
# [1, 1]