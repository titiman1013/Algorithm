import sys; sys.stdin = open('text1.txt', 'r')

# reculsive fail

# def check(pos, sec):
#     global min_sec, K

#     if pos == K:
#         if sec < min_sec:
#             min_sec = sec
#         return

#     if pos > K:
#         check(pos - 1, sec + 1)

#     else:
#         check(pos + 1, sec + 1)
#         check(pos * 2, sec + 1)



# N, K = map(int, input().split())

# min_sec = 100000000
# res = check(N, 0)
# print(min_sec)