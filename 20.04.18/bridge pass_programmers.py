def solution(stones, k):
    answer = 0

    while True:
        position = 0
        jump = 1
        while position < len(stones):
            if stones[position] != 0:
                stones[position] -= 1
                position += 1
                jump = 1
            else:
                jump += 1
                if stones[position] != 0:
                    stones[position] -= 1
                position += 1
            if jump > k:
                print(position)
                return answer
        answer += 1
        print(stones)

    return answer






print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3))
# 결과: 3

print(solution([2, 1, 2, 1, 2], 3))
# 결과: 2