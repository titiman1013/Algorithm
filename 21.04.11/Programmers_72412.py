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



# 창완1

import bisect

def solution(info, query):
    answer = []
    index_dict = {'-':0,
    'cpp': 1,
    'java':2,
    'python': 3,
    'backend':1,
    'frontend' :2,
    'junior':1,
    'senior':2,
    'chicken':1,
    'pizza':2,
    }
    store_query = [[] for _ in range(108)]
    for info_string in info:
        language,position,career,soulfood,score = info_string.split(' ')
        score = int(score)
        for ind1 in [0,index_dict[language]]:
            for ind2 in [0,index_dict[position]]:
                for ind3 in [0,index_dict[career]]:
                    for ind4 in [0,index_dict[soulfood]]:
                        ind = ind1*27 + ind2*9 + ind3*3 + ind4
                        bisect.insort(store_query[ind],score)

    for qu in query:
        language,position,career,last_query = map(str.strip,qu.split('and'))
        soulfood,score = last_query.split(' ')
        score = int(score)
        ind = index_dict[language]*27 + index_dict[position]*9 + index_dict[career]*3 + index_dict[soulfood]
        cnt = len(store_query[ind]) - bisect.bisect_left(store_query[ind],score)
        answer.append(cnt)
    

    return answer


# 창완2

from itertools import combinations

def solution(info, query):
    answer = []
    languages = ['cpp','java','python','-']
    positions = ['backend','frontend','-']
    careers = ['junior','senior','-']
    soulfoods = ['chicken','pizza','-']
    total_dict = {language : {position : {career : {soulfood : [0]*100001 for soulfood in soulfoods} for career in careers}  for position in positions} for language in languages}
    for info_string in info:
        language,position,career,soulfood,score = info_string.split(' ')
        score = int(score)
        info_list = [language,position,career,soulfood]
        for i in range(1<<4):
            temp = []
            for j in range(4):
                if i&(1<<j):
                    temp.append(info_list[j])
                else:
                    temp.append('-')
            total_dict[temp[0]][temp[1]][temp[2]][temp[3]][score] += 1
    for language in total_dict.keys():
        for position in total_dict[language].keys():
            for career in total_dict[language][position].keys():
                for soulfood in total_dict[language][position][career].keys():
                    for score in range(1,100001):
                        total_dict[language][position][career][soulfood][score] += total_dict[language][position][career][soulfood][score-1]
    for query_string in query:
        language,position,career,last_query = map(str.strip,query_string.split('and'))
        soulfood,score = last_query.split(' ')
        score = int(score)
        answer.append(total_dict[language][position][career][soulfood][100000] - total_dict[language][position][career][soulfood][score-1])
    return answer


# 창완3

def solution(info, query):
    answer = []
    index_dict = {'-':0,
    'cpp': 1,
    'java':2,
    'python': 3,
    'backend':1,
    'frontend' :2,
    'junior':1,
    'senior':2,
    'chicken':1,
    'pizza':2,
    }
    store_query = [[0]*100001 for _ in range(108)]
    for info_string in info:
        language,position,career,soulfood,score = info_string.split(' ')
        score = int(score)
        for ind1 in [0,index_dict[language]]:
            for ind2 in [0,index_dict[position]]:
                for ind3 in [0,index_dict[career]]:
                    for ind4 in [0,index_dict[soulfood]]:
                        ind = ind1*27 + ind2*9 + ind3*3 + ind4
                        store_query[ind][score] += 1
    for ind in range(108):
        for score in range(1,100001):
            store_query[ind][score] += store_query[ind][score-1]

    for qu in query:
        language,position,career,last_query = map(str.strip,qu.split('and'))
        soulfood,score = last_query.split(' ')
        score = int(score)
        ind = index_dict[language]*27 + index_dict[position]*9 + index_dict[career]*3 + index_dict[soulfood]
        answer.append(store_query[ind][100000] - store_query[ind][score-1])
    

    return answer






print(solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"], ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]))

# answer
# [1,1,1,1,2,4]