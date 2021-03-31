def solution(s):
    answer = ''

    up = True
    for string in s:
        if string == ' ':
            answer += ' '
            up = True
        else:
            if up:
                answer += string.upper()
                up = False
            else:
                answer += string.lower()

    return answer

    # return s.title()




print(solution("3people unFollowed me"))
print(solution("for the last week"))

# answer
# "3people Unfollowed Me"
# "For The Last Week"