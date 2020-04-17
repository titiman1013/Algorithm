#
# def solution(user_id, banned_id):
#     answer = 0
#     temp = []
#     for _ in range(len(user_id)):
#         check_u = [0 for _ in range(len(user_id))]
#         check_b = [0 for _ in range(len(banned_id))]
#         for i in range(len(user_id)):
#             for j in range(len(banned_id)):
#                 if check_b[j] == 0:
#                     if len(user_id[i]) == len(banned_id[j]):
#                     # if user_id[i][0] == banned_id[j][0] or banned_id[j][0] == '*':
#                         for k in range(len(user_id)):
#                             if user_id[i][k] == banned_id[j][k] or banned_id[j][k] == '*':
#                                 pass
#                             else:
#                                 break
#                         else:
#                             check_u[i] += 1
#                             check_b[j] = 1
#                             break
#         # print(check_u)
#         if sum(check_u) == len(banned_id):
#             if check_u not in temp:
#                 temp.append(check_u)
#                 answer += 1
#     print(temp)
#     return answer




#
answer = 0
def solution(user_id, banned_id):
    global answer
    


    return answer




# 1
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "abc1**"]))
# result = 2

# 2
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["*rodo", "*rodo", "******"]))
# result = 2

# 3
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "*rodo", "******", "******"]))
# result = 3