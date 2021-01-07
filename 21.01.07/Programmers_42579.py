def solution(genres, plays):
    dic = {}
    for i in range(len(genres)):
        if genres[i] in dic:
            dic[genres[i]][i] = plays[i]
        else:
            dic[genres[i]] = {}
            dic[genres[i]][i] = plays[i]
    
    # 장르별로 정렬
    dic_genre = sorted(dic.items(), key=lambda x: sum(x[1].values()), reverse=True)
    
    # 재생회수별로 정렬
    dic_play = {}
    for genre, play_lst in dic_genre:
        dic_play[genre] = sorted(play_lst.items(), key=lambda x: x[1], reverse=True)
    
    answer = []
    for genre in dic_play.keys():
        for idx, val in enumerate(dic_play[genre]):
            answer.append(val[0])
            if idx == 1:
                break
    
    return answer

    
    # answer = []
    # return answer




print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))