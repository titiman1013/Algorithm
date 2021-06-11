# give up

def solution(msg):
    answer = []

    dictionary = {chr(i): i - 64 for i in range(65, 91)}
    idx = 0
    numbering = 27
    w, c = msg[0], msg[1]
    while idx < len(msg):
        answer.append(dictionary.get(w))
        
        # end = 1
        # print(w, dictionary.get(msg[idx:idx + end]))
        # while dictionary.get(msg[idx:idx + end]) == None:
        #     end += 1
        # print(msg[idx:idx + end + 1])
        # dictionary[msg[idx:idx + end + 1]] = numbering
        # numbering += 1

        # idx += end
        # w, c = c, msg[idx + 1]

        dictionary[w + c] = numbering
        numbering += 1

        idx += len(c)
        cnt = 1
        while dictionary.get(msg[idx:idx + cnt]):
            if idx + cnt < len(msg):
                cnt += 1
        

    return answer





print(solution('KAKAO'))
print(solution('TOBEORNOTTOBEORTOBEORNOT'))
print(solution('ABABABABABABABAB'))

# answer
# [11, 1, 27, 15]
# [20, 15, 2, 5, 15, 18, 14, 15, 20, 27, 29, 31, 36, 30, 32, 34]
# [1, 2, 27, 29, 28, 31, 30]