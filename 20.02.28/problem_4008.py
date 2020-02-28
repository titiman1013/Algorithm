import sys
sys.stdin = open("숫자만들기.txt", "r")

# def insert(cnt):
#     global maximum
#     global minimum
#     global nums
#     if cnt == len(check):
#         clone = nums
#         for i in range(len(check)):
#             if check[i] == True:
#                 clone[(i*2)+1] = operator_list[i]
#                 print(clone)
#         return
                

#     check[cnt] = True
#     insert(cnt+1)
#     check[cnt] = False
#     insert(cnt+1)


# # def calc():
# #     pass



# T = int(input())
# for t in range(T):
#     N = int(input())
#     operator = list(map(int, input().split()))
#     operator_dict = {}
#     for idx, oper in enumerate(operator):
#         if idx == 0:
#             operator_dict['+'] = oper
#         if idx == 1:
#             operator_dict['-'] = oper
#         if idx == 2:
#             operator_dict['*'] = oper
#         if idx == 3:    
#             operator_dict['/'] = oper
#     operator_list = []
#     for key, val in operator_dict.items():
#         if val != 0:
#             while val != 0:
#                 operator_list.append(key)
#                 val -= 1
                
#     nums = input()
#     maximum = 0
#     minimum = 0
#     check = [False] * len(operator_list)
#     insert(0)
   
#     print(f'#{t+1} {maximum-minimum}')


T = int(input())
for t in range(T):
    N = int(input())
    