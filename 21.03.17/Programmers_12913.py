# false

def solution(land):
    answer = 0

    pos = -1
    for row_idx in range(len(land)):
        max_idx = -1
        max = 0
        for col_idx, num in enumerate(land[row_idx]):
            if num > max and col_idx != pos:
                max_idx, max = col_idx, num
        pos = max_idx
        answer += max
    
    return answer



print(solution([[1,2,3,5],[5,6,7,8],[4,3,2,1]]))

# answer
# 16