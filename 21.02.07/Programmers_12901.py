def solution(a, b):
    answer = ''

    t0 = [4, 6, 9, 11]
    t1 = [1, 3, 5, 7, 8, 10, 12]
    t9 = [2]
    day = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']

    date = 0
    for i in range(1, a):
        if i in t0:
            date += 30
        elif i in t1:
            date += 31
        else:
            date += 29
    date += b - 1

    answer = day[(5 + date) % 7]

    return answer




print(solution(5, 24))