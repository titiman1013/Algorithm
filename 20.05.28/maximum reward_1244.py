import sys; sys.stdin = open('maximum reward.txt', 'r')

# 실패
# def check(cnt, number):
#     global reward, exchange, str_reward, list_reward, res
#     if cnt == exchange:
#         if number > res:
#             res = number
#         return

#     come = 0
#     max_temp = 0
#     max_temp_i = 0
#     min_temp = 10
#     min_temp_i = 0
#     for i in range(len(list_reward)):
#         if list_reward[i] >= max_temp and visited[i] == 0:
#             max_temp = list_reward[i]
#             max_temp_i = i
#     # print(max_temp_i)
#     if max_temp_i == cnt:
#         come = 1
#         max_temp = 0
#         for i in range(len(list_reward)):
#             if list_reward[i] >= max_temp and visited[i] == 0 and i != cnt:
#                 max_temp = list_reward[i]
#                 max_temp_i = i
#             if list_reward[i] < min_temp:
#                 min_temp = list_reward[i]
#                 min_temp_i = i
            
#     if come == 0:
#         a = list_reward[max_temp_i]
#         b = list_reward[cnt]
#         list_reward[cnt] = a
#         list_reward[max_temp_i] = b
#     else:
#         a = list_reward[max_temp_i]
#         b = list_reward[min_temp_i]
#         list_reward[min_temp_i] = a
#         list_reward[max_temp_i] = b
#         visited[max_temp_i] = 1
#     visited[cnt] = 1 

#     str_temp = ''
#     for i in range(len(list_reward)):
#         str_temp += str(list_reward[i])

#     str_reward = str_temp
#     reward = int(str_reward)

#     print(reward)
#     print(visited)
#     check(cnt+1, reward)
    


# for tc in range(1, int(input())+1):
#     str_reward, str_exchange = input().split()

#     reward, exchange = int(str_reward), int(str_exchange)
#     list_reward = list(map(int, list(str_reward)))
#     res = 0
#     visited = [0] * len(str_reward)
#     # print(visited)
#     check(0, reward)
#     # print(list_reward)

#     print(f'#{tc} {res}')



# 
for tc in range(1, int(input())+1):
    