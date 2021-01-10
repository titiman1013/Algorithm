def solution(n, results):
    answer = 0

    wins, loses = {}, {}
    for i in range(1, n + 1):
        wins[i], loses[i] = set(), set()
    
    for i in range(1, n + 1):
        for winner, loser in results:
            if winner == i:
                wins[i].add(loser)
            if loser == i:
                loses[i].add(winner)
        
        # i를 이기는 사람은 i가 이기는 사람들을 다 이긴다
        for win_to_i in loses[i]:
            wins[win_to_i].update(wins[i])
        # i에게 지는 사람은 i를 이긴 사람들에게 다 진다
        for lose_to_i in wins[i]:
            loses[lose_to_i].update(loses[i])

    # 본인을 뺀 남은 사람과의 승패정보를 전부 가지고 있다면 순위를 매길 수 있는 사람
    for i in range(1, n + 1):
        if len(wins[i]) + len(loses[i]) == n - 1:
            answer += 1

    return answer




print(solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))

# answer
# 2