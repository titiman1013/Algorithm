def solution(record):
    answer = []

    id_dict = dict()
    for message in record:
        log = list(map(str, message.split()))
        if len(log) == 3:
            behavior, id, nickname = log
            if id_dict.get(id) != nickname:
                id_dict[id] = nickname
    
    for message in record:
        log = list(map(str, message.split()))
        if log[0] == 'Enter':
            answer.append(f'{id_dict[log[1]]}님이 들어왔습니다.')
        elif log[0] == 'Leave':
            answer.append(f'{id_dict[log[1]]}님이 나갔습니다.')

    return answer




print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))

# answer
# ["Prodo님이 들어왔습니다.", "Ryan님이 들어왔습니다.", "Prodo님이 나갔습니다.", "Prodo님이 들어왔습니다."]