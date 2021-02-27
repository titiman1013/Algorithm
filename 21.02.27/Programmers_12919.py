def solution(seoul):
    answer = ''

    for idx, val in enumerate(seoul):
        if val == "Kim":
            answer = "김서방은 " + str(idx) + "에 있다"
            break

    return answer




print(solution(["Jane", "Kim"]))

# answer
# "김서방은 1에 있다"