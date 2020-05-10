import sys; sys.stdin = open('win rate.txt', 'r')

answer = []
T = int(input())
for i in range(T) :
    parameter = input().split(" ")
    if int(parameter[0]) / int(parameter[1]) > int(parameter[2]) / int(parameter[3]) :
        answer.append("ALICE")
    elif int(parameter[0]) / int(parameter[1]) < int(parameter[2]) / int(parameter[3]) :
        answer.append("BOB")
    else :
        answer.append("DRAW")
for i in range(T) :
    print("#{} {}".format(i+1, answer[i]))