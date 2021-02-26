def solution(s):
    answer = True

    return s.isdecimal() and (len(s) == 4 or len(s) == 6)




print(solution("a234"))
print(solution("1234"))

# answer
# false
# true