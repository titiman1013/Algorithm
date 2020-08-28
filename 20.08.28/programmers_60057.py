# string compression


# 1
# def solution(s):
#     answer = len(s)
#     for str_len in range(1, len(s)//2+1):
#         temp = 0
#         start = 0
#         end = str_len
#         repeat_str = ""
#         cnt = 1
#         remain = 0
#         while end < len(s):
#             if len(repeat_str) < str_len:
#                 repeat_str = s[start:end]
#             else:
#                 if repeat_str == s[end:end+str_len]:
#                     cnt += 1
#                     start += str_len
#                     end += str_len
#                 else:
#                     repeat_str = s[end:end+str_len]
#                     if cnt > 1:
#                         cnt = 1
#                         temp += 1
#                     temp += str_len
#                     start = end
#                     if end + str_len > len(s):
#                         remain = len(s) - end 
#                     end += str_len
#         # print(cnt)
#         if cnt > 1:
#             temp += (len(str(cnt)) + str_len)
#         if remain:
#             temp += remain
#         # print(temp)
#         if temp < answer:
#             answer = temp
#         # print(answer)

#     return answer


#2
def solution(s):
    answer = len(s)
    for str_len in range(1, len(s)//2 + 1):
        temp = 0
        cnt = 1
        remain = 0
        for i in range(0, len(s), str_len):
            if s[i:i+str_len] == s[i+str_len:i+str_len*2]:
                cnt += 1
            else:
                if cnt > 1:
                    temp += len(str(cnt))
                    cnt = 1
                temp += str_len
                if i + str_len > len(s):
                    remain = len(s) - i - str_len
                    break
        if remain:
            temp += remain
        if temp < answer:
            answer = temp 
        # print(temp)
    return answer


print(solution("aabbaccc"))
print(solution("ababcdcdababcdcd"))
print(solution("abcabcdede"))
print(solution("abcabcabcabcdededededede"))
print(solution("xababcdcdababcdcd"))
print(solution("a"))
print(solution("aaaaaaaaaa"))