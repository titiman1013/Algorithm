# time over

# def solution(info, query):
#     answer = []

#     for condition in query:
#         lang, pos, career, food_score = map(str, condition.split(' and '))
#         food, score = map(str, food_score.split())
#         cnt = 0
#         for resume in info:
#             # applicant
#             a_lang, a_pos, a_career, a_food, a_score = map(str, resume.split())
#             if (lang == '-' or lang == a_lang) and (pos == '-' or pos == a_pos) and (career == '-' or career == a_career) and (food == '-' or food == a_food) and int(score) <= int(a_score):
#                 cnt += 1
#         answer.append(cnt)

#     return answer


#

def solution(info, query):
    answer = []

    resumes = dict()
    # applicant
    for val in info:
        idx = len(val) - 1
        for i in range(idx - 1, -1, -1):
            if val[i].isnumeric():
                idx -= 1
            else:
                break
        person = val[:idx]
        if resumes.get(int(val[idx:])):
            resumes[int(val[idx:])].append(list(map(str, person.split())) + ['-'])
        else:
            resumes[int(val[idx:])] = [list(map(str, person.split())) + ['-']]
    
    score_lists = sorted(resumes, reverse=True)
    
    for condition in query:
        lang, pos, career, food_score = map(str, condition.split(' and '))
        food, score = map(str, food_score.split())
        cnt = 0
        for score_list in score_lists:
            if int(score) <= score_list:
                needs = resumes.get(score_list)
                for need in needs:
                    if lang in need and pos in need and career in need and food in need:
                        cnt += 1
            else: break
            
        answer.append(cnt)

    return answer




print(solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"], ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]))

# answer
# [1,1,1,1,2,4]