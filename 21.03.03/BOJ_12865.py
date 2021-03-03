import sys; sys.stdin = open('12865.txt', 'r')

def reculsive(idx, weight, satis):
    global answer

    if idx == N:
        if weight <= K:
            if satis > answer:
                answer = satis
        return

    reculsive(idx+1, weight+loads[idx][0], satis+loads[idx][1])
    reculsive(idx+1, weight, satis)



# N: 물건 개수, K: 들 수 있는 무게
N, K = map(int, input().split())
# W: 물건 무게, V: 가치
loads = [list(map(int, input().split())) for _ in range(N)]

answer = 0
reculsive(0, 0, 0)
print(answer)