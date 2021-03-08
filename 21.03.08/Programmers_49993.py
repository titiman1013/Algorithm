def check(answer, skill_tree, sequence):
    flag = 0
    for seq in skill_tree:
        if seq in sequence:
            if flag < sequence.get(seq):
                return 0
            flag += 1
    return 1
            


def solution(skill, skill_trees):
    answer = 0

    sequence = {val: idx for idx, val in enumerate(skill)}

    for skill_tree in skill_trees:
        answer += check(answer, skill_tree, sequence)

    return answer




print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"]))

# answer
# 2