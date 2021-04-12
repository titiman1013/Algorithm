# false

# def solution(k, room_number):
#     answer = []

#     room = [False] * (k + 1)
#     for prefer_num in room_number:
#         if room[prefer_num]:
#             while room[prefer_num]:
#                 prefer_num += 1
#         answer.append(prefer_num)
#         room[prefer_num] = True

#     return answer


# false

# def solution(k, room_number):
#     answer = []

#     room = dict()
#     for prefer_num in room_number:
#         if room.get(prefer_num):
#             while room.get(prefer_num):
#                 prefer_num += 1
#         answer.append(prefer_num)
#         room[prefer_num] = True

#     return answer


# false

def solution(k, room_number):
    answer = []
    
    room = []
    for prefer_num in room_number:
        if prefer_num in room:
            while prefer_num in room:
                prefer_num += 1
        room.append(prefer_num)
    
    return room




print(solution(10, [1,3,4,1,3,1]))

# answer
# [1,3,4,2,5,6]