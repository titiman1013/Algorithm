import sys
sys.stdin = open("은행업무.txt", "r")

# T = int(input())
# for t in range(T):
#     m_second = list(map(int, list(input())))
#     m_third = list(map(int, list(input())))
    # print(m_second, m_third)
    
    # second = [0]
    # third = [0]

    # n = 0
    # while n != 6:
    #     n += 1
    #     second[-1] += 1
    #     third[-1] += 1
    #     for i in range(len(second)-1, -1, -1):
    #         if second[i] == 2:
    #             second[i] = 0
    #             second.insert(i, 0)
                
    #         if second[0] == 0:
    #             second[0] = 1

    
    # second = [0]
    # third = [0]

    # n = 0
    # while n != 2:
    #     n += 1
    #     second[-1] += 1
    #     third[-1] += 1
    #     for i in range(len(second)-1, -1, -1):
    #         if second[i] == 2:
    #             second[i] = 0
                
    #             if second[0] == 0:
    #                 second.insert[0, 1]
    #             else:
    #                 second[i-1] += 1


    # print(second)











T = int(input())
for t in range(T):
    m_second = list(map(int, list(input())))
    m_third = list(map(int, list(input())))
    # print(m_second, m_third)
    
    second = [0]
    third = [0]
    n = 0
    result = 0
    while True:
        n += 1
        # 2진수
        second[-1] += 1
        for i in range(len(second)-1, -1, -1):
            if second[i] == 2:
                if i != 0:
                    second[i-1] += 1
                second[i] = 0
                if second[0] == 0:
                    second.insert(0, 1)

        # 3진수
        third[-1] += 1
        for i in range(len(third)-1, -1, -1):
            if third[i] == 3:
                if i != 0:
                    third[i-1] += 1
                third[i] = 0
                if third[0] == 0:
                    third.insert(0, 1)

        # 자릿수 확인
        if len(m_second) != len(second) or len(m_third) != len(third):
            continue

        # 2진수 판별
        check_2 = 0
        for i in range(len(second)):
            if m_second[i] != second[i]:
                check_2 += 1
                if check_2 > 1:
                    break

        # 3진수 판별
        check_3 = 0
        for i in range(len(third)):
            if m_third[i] != third[i]:
                check_3 += 1
                if check_3 > 1:
                    break
        
        # 전체 판별
        if check_2 == 1 and check_3 == 1:
            result = n
            break
    
    print(f'#{t+1} {result}')