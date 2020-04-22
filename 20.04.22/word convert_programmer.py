#
def solution(begin, target, words):
    answer = 0
    temp_list = []
    while begin != target:
        if words:
            for i in range(len(words)):
                temp = 0
                for j in range(len(begin)):
                    if begin[j] == words[i][j]:
                        temp += 1
                if temp == len(begin)-1:
                    begin = words[i]
                    temp_list.append(words[i])
                    words.pop(i)
                    answer += 1
                    # print(begin)
                    # print(words)
                    # print(temp_list)
                    # print(answer)
                    break
            else:
                if len(temp_list) > 1:
                    answer -= 2
                    begin = temp_list[-2]
                    temp_list.pop(-2)
                else:
                    answer = 0
                    words.clear()
                    break
        else:
            answer = 0
            break

    return answer


# #
# answer = 0
# cnt = 0
# def solution(begin, target, words):
#     global answer
#     global cnt

#     if begin == target:
#         return answer
#     # temp = 0
#     # for i in range(len(begin)):
#     #     if begin[i] == words[cnt][i]:
#     #         temp += 1
#     # if temp == len(begin)-1:
#     #     begin = words[cnt]
#     #     answer += 1
#     #     words.pop(cnt)
#     #     return

#     answer += 1
#     solution(begin, target, words)
#     answer -= 1
#     solution(begin, target, words)

#     return answer



# #
# def solution(begin, target, words):
#     answer = 0

#     return answer









# #
# def solution(begin, target, words):
#     words = set(words)

#     q = [(begin, 0)]

#     for word, cnt in q:
#         if word == target:
#             return cnt

#         for idx in range(0, len(word)):
#             for char in 'abcdefghijklmnopqrstuvwxyz':
#                 tmp = word[:idx] + char + word[idx + 1:]

#                 if tmp in words:
#                     q.append([tmp, cnt + 1])
#                     words.remove(tmp)

#     return 0



# # 예지
# # bfs 개념 활용
# def solution(begin, target, words):
#     if target not in words:
#         answer = 0
#     else:
#         result = {begin:0}
#         stack = [begin]
#         visit = [0] * len(words)
#         while stack:
#             begin = stack.pop(0)
#             for word in words:
#                 cnt = 0
#                 for k in range(len(word)):
#                     if word[k] == begin[k]:
#                         cnt += 1
#                     if cnt != 2:
#                         break
#                 else:
#                     idx = words.index(word)
#                     if visit[idx] == 0:
#                         visit[idx] = 1
#                         stack.append(word)
#                         result[word] = result[begin] + 1
#         answer = result.get(target)
#     return answer









print(solution("hit", "cog", ['hot', 'dot', 'dog', 'lot', 'log', 'cog']))
# 4

# print(solution("hit", "cog", ['hot', 'dot', 'dog', 'lot', 'log']))
# 0


