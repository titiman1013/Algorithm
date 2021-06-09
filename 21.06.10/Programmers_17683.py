# runtime error

# def solution(m, musicinfos):
#     answer = '(None)'

#     play_time = 0
#     for musicinfo in musicinfos:
#         start, end, title, codes = map(str, musicinfo.split(','))
#         for idx, code in enumerate(codes):
#             if code == m[0]:
#                 cnt = 1
#                 code_idx = idx
#                 while cnt < len(m):
#                     # print(idx, cnt)
#                     if m[cnt] == codes[code_idx + cnt]:
#                         if code_idx + cnt >= len(codes) - 1:
#                             code_idx = -cnt - 1
#                         cnt += 1
#                     else:
#                         break
                
#                 else:
#                     if code_idx + cnt < len(codes):
#                         if codes[code_idx + cnt] == '#':
#                             continue
                    
#                     if cnt == len(m):
#                         if answer == "(None)":
#                             answer = title
#                             play_time = (int(end[:2]) - int(start[:2])) * 60 + (int(end[3:]) - int(start[3:]))
#                         else:
#                             if play_time < (int(end[:2]) - int(start[:2])) * 60 + (int(end[3:]) - int(start[3:])):
#                                 answer = title
#                                 play_time = (int(end[:2]) - int(start[:2])) * 60 + (int(end[3:]) - int(start[3:]))
                        
#     return answer



# false

# def code_reform(codes):
#     codes = codes.replace('C#', 'c')
#     codes = codes.replace('D#', 'd')
#     codes = codes.replace('F#', 'f')
#     codes = codes.replace('G#', 'g')
#     codes = codes.replace('A#', 'a')

#     return codes


# def solution(m, musicinfos):
#     answer = ''

#     m = code_reform(m)

#     play_time = 0
#     for musicinfo in musicinfos:
#         start, end, title, codes = map(str, musicinfo.split(','))
#         codes = code_reform(codes)

#         if len(m) <= len(codes):
#             if m not in codes * 2: continue
#         else:
#             if codes not in m * 2: continue

#         if answer:
#             if play_time >= (int(end[:2]) - int(start[:2])) * 60 + (int(end[3:]) - int(start[3:])): continue
        
#         answer = title
#         play_time = (int(end[:2]) - int(start[:2])) * 60 + (int(end[3:]) - int(start[3:]))
        
#     return answer if answer else '(None)'



#

def code_reform(codes):
    codes = codes.replace('C#', 'c')
    codes = codes.replace('D#', 'd')
    codes = codes.replace('F#', 'f')
    codes = codes.replace('G#', 'g')
    codes = codes.replace('A#', 'a')

    return codes


def solution(m, musicinfos):
    answer = ''

    m = code_reform(m)

    max_play_time = 0
    for musicinfo in musicinfos:
        start, end, title, codes = map(str, musicinfo.split(','))
        codes = code_reform(codes)

        play_time = (int(end[:2]) - int(start[:2])) * 60 + (int(end[3:]) - int(start[3:]))
        idx = 0
        play_codes = ''
        play = play_time
        while play:
            play_codes += codes[idx]
            if idx + 1 == len(codes):
                idx = -1
            idx += 1
            play -= 1
        
        if m in play_codes:
            if answer:
                if max_play_time >= play_time: continue
            max_play_time = play_time
            answer = title
                    
        
    return answer if answer else '(None)'






print(solution("ABCDEFG", ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]))
print(solution("CC#BCC#BCC#BCC#B", ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]))
print(solution("ABC", ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]))
print(solution("AAA", ["12:00,12:03,1,AAA", "12:00,12:04,2,AAA", "12:00,12:03,3,AAA"]))

# answer
# "HELLO"
# "FOO"
# "WORLD"