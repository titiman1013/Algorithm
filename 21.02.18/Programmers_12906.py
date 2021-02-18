# def solution(arr):
#     answer = []

#     for val in arr:
#         if answer:
#             if answer[-1] == val:
#                 continue
#         answer.append(val)

#     return answer



# slicing

# 빈 array을 슬라이싱해도 error가 발생하지 않음

def solution(arr):
    a = []
    for i in arr:
        if a[-1:] == [i]: continue
        a.append(i)
    return a




print(solution([1,1,3,3,0,1,1]))
print(solution([4,4,4,3,3]))

# answer
# [1, 3, 0, 1]
# [4, 3]