import sys; sys.stdin = open('view.txt', 'r')

for i in range(1, 11):
    title = input()
    buildings = list(map(int, input().split()))
    result = 0
    for j in range(len(buildings)-2):
        if j > 1:
            floor_list = []
            if buildings[j] > buildings[j-1] and buildings[j] > buildings[j-2] and buildings[j] > buildings[j+1] and buildings[j] > buildings[j+2]:
                floor_list.append(buildings[j-2])
                floor_list.append(buildings[j-1])
                floor_list.append(buildings[j+1])
                floor_list.append(buildings[j+2])
                high = max(floor_list)
                result += buildings[j] - high
    print("#{} {}".format(i, result))