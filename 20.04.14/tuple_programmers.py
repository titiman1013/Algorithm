def solution(s):
    answer = []
    # print(s)
    s = s.split('},{')
    s[0] = s[0][2:]
    s[-1] = s[-1][:-2]
    for i in range(len(s)):
        s[i] = list(map(int, s[i].split(',')))
    # print(s)
    for i in range(len(s)):
        for j in range(len(s)):
            if len(s[j]) == i + 1:
                # print(s[j])
                for k in range(len(s[j])):
                    if int(s[j][k]) not in answer:
                        answer.append(int(s[j][k]))
                break
    return answer






# print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))
# [2, 1, 3, 4]

# print(solution("{{1,2,3},{2,1},{1,2,4,3},{2}}"))
# # [2, 1, 3, 4]

# print(solution("{{20,111},{111}}"))
# # [111, 20]

# print(solution("{{123}}"))
# # [123]

# print(solution({{4,2,3},{3},{2,3,4,1},{2,3}}))
# # [3, 2, 4, 1]

print(solution("{{10,9,8,7,6,5,4,3,2,1},{1},{9,8,7,6,5,4,3,2,1},{1,2},{8,7,6,5,4,3,2,1},{1,2,3},{7,6,5,4,3,2,1},{1,2,3,4},{6,5,4,3,2,1},{1,2,3,4,5}}"))