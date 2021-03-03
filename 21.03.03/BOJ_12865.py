import sys; sys.stdin = open('12865.txt', 'r')

# # N: 물건 개수, K: 들 수 있는 무게
N, K = map(int, input().split())
# # W: 물건 무게, V: 가치
loads = [list(map(int, input().split())) for _ in range(N)]