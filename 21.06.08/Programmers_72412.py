from collections import defaultdict
import bisect

def solution(info, query):
    answer = []

    case_nums = {
        '-': 0,
        'cpp': 1,
        'java': 2,
        'python': 3,
        'backend': 1,
        'frontend': 2,
        'junior': 1,
        'senior': 2,
        'chicken': 1,
        'pizza': 2,
    }

    # all_case = defaultdict(dict)
    all_case = defaultdict(list)
    for applicant in info:
        language, task, career, food, score = map(str, applicant.split())
        
        for l_n in [0, case_nums[language]]:
            for t_n in [0, case_nums[task]]:
                for c_n in [0, case_nums[career]]:
                    for f_n in [0, case_nums[food]]:
                        key_num = str(l_n) + str(t_n) + str(c_n) + str(f_n)
                        # all_case[key_num][int(score)] = all_case[key_num].get(int(score), 0) + 1
                        all_case[key_num].append(int(score))

    for case in all_case.keys():
        all_case[case].sort()
    
    for requirements in query:
        requirement = list(map(str, requirements.split()))
        
        # total = 0
        score_list = all_case.get(str(case_nums[requirement[0]]) + str(case_nums[requirement[2]]) + str(case_nums[requirement[4]]) + str(case_nums[requirement[6]]))
        required_score = int(requirement[7])
        if score_list:
            # for score, cnt in score_list.items():
            #     if score >= required_score:
            #         total += cnt
            answer.append(len(score_list) - bisect.bisect_left(score_list, required_score))

        # answer.append(total)
        else:
            answer.append(0)

    return answer




print(solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"], ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]))

# answer
# [1,1,1,1,2,4]