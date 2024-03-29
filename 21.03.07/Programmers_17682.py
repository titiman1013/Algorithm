def solution(dartResult):
    answer = 0

    score_list = []
    score_idx = -1
    idx = 0
    while idx < len(dartResult):
        if dartResult[idx].isdigit():
            num_idx = idx
            while dartResult[num_idx].isdigit():
                num_idx += 1
            if dartResult[num_idx] == 'S':
                score_list.append(int(dartResult[idx:num_idx]))
            elif dartResult[num_idx] == 'D':
                score_list.append(int(dartResult[idx:num_idx]) ** 2)
            elif dartResult[num_idx] == 'T':
                score_list.append(int(dartResult[idx:num_idx]) ** 3)
            score_idx += 1
            idx = num_idx + 1
        else:
            if dartResult[idx] == '*':
                if score_idx == 0:
                    score_list[score_idx] *= 2
                else:
                    score_list[score_idx - 1] *= 2
                    score_list[score_idx] *= 2
            elif dartResult[idx] == '#':
                score_list[score_idx] *= -1
            idx += 1
    
    answer = sum(score_list)

    return answer


# re.compile 정규식 확인하기




print(solution("1S2D*3T"))
print(solution("1D2S#10S"))
print(solution("1D2S0T"))
print(solution("1S*2T*3S"))
print(solution("1D#2S*3S"))
print(solution("1T2D3D#"))
print(solution("1D2S3T*"))

# answer
# 37
# 9
# 3
# 23
# 5
# -4
# 59