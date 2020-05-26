import sys; sys.stdin = open('number jump.txt', 'r')

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def go(x, y, cnt, _sum):
    if cnt == 6:
        if _sum not in res_list:
            res_list.append(_sum)
        return

    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < 5 and 0 <= ny < 5:
            go(nx, ny, cnt+1, _sum+arr[nx][ny])

arr = [input().split() for _ in range(5)]
# arr = [list(map(str, input().split())) for _ in range(5)]
# arr = [list(map(int, list(input().split()))) for _ in range(5)]
# print(arr)

res_list = []
for i in range(5):
    for j in range(5):
        go(i, j, 1, arr[i][j])

# print(res_list)
print(len(res_list))


# # 
# def checkNumber(board, pos, unique_numbers, current_number, count):
#     rd = [-1, 0, 1, 0]
#     cd = [0, 1, 0, -1]
#     r, c = pos
 
#     for i in range(4):
#         temp_r = r + rd[i]
#         temp_c = c + cd[i]
#         if 0 <= temp_r < 5 and 0 <= temp_c < 5:
#             next_number = current_number + str(board[temp_r][temp_c])
#             if count == 5:
#                 unique_numbers.add(next_number)
#             else:
#                 checkNumber(board, (temp_r, temp_c), unique_numbers, next_number, count + 1)
 
 
 
# def solve(board):
#     unique_numbers = set()
#     for i in range(5*5):
#         r = i // 5
#         c = i % 5
#         checkNumber(board, (r,c), unique_numbers, str(board[r][c]), 1)
#     total_unique_count = len(unique_numbers)
#     print(total_unique_count)
 
 

# lines = []
# for i in range(5):
#     lines.append(input().strip().split())
# solve(lines)