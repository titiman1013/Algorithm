def solution(absolutes, signs):
    answer = 123456789

    answer = sum(absolutes[i] if signs[i] else -absolutes[i] for i in range(len(absolutes)))

    return answer




print(solution([4,7,12], [True, False, True]))
print(solution([1,2,3], [False, False, True]))

# answer
# 9
# 0