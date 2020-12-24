import sys; sys.stdin = open('text1.txt', 'r')

for tc in range(1, int(input()) + 1):
    # F: 전체 층, S: 현재 층, G: 스타트링크 위치, U: Up Btn, D: Down Btn
    F, S, G, U, D = map(int, input().split())
    