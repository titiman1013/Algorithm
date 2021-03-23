from datetime import datetime, timedelta

def solution(lines):
    answer = 0

    # print(True if "2016-09-15 01:00:04.001" < "2016-09-16 01:00:07.000" else False)
    # print(True if datetime.strptime("2016-09-16 01:00:07.000", '%Y-%m-%d %H:%M:%S.%f') < datetime.strptime("2016-09-15 01:00:04.001", '%Y-%m-%d %H:%M:%S.%f') else False)
    lines_list = [list(line.split()) for line in lines]
    start_end_times = []
    check_times = []
    for D, S, T in lines_list:
        # 끝에서 -1ms를 해준 값까지 포함되므로
        mili_sec = int(round(float(T[:-1]), 3) * 1000 - 1)
        end = datetime.strptime(D + ' ' + S, "%Y-%m-%d %H:%M:%S.%f")
        start = end - timedelta(milliseconds=mili_sec)
        # for문을 돌리기위한 (시작점, 끝점)을 리스트에 저장
        start_end_times.append((start, end))
        # 체크해야 할 시작점과 끝점 저장
        check_times.append(start)
        check_times.append(end)
    
    cnt_list = []
    for i in range(len(check_times)):
        traffic_start = check_times[i]
        traffic_end = traffic_start + timedelta(milliseconds=999)
        cnt = 0
        for start, end in start_end_times:
            # 끝점이 트래픽 시간에 포함
            if start <= traffic_start and end >= traffic_start:
                cnt += 1
            # 시작점이 트래픽 시간에 포함
            elif start <= traffic_end and end >= traffic_end:
                cnt += 1
            # 모든부분이 트래픽 시간에 포함
            elif start >= traffic_start and end <= traffic_end:
                cnt += 1
        cnt_list.append(cnt)

    answer = max(cnt_list)

    return answer





print(solution([
    "2016-09-15 01:00:04.001 2.0s", 
    "2016-09-15 01:00:07.000 2s"
]))
print(solution([
    "2016-09-15 01:00:04.002 2.0s", 
    "2016-09-15 01:00:07.000 2s"
]))
print(solution([
    "2016-09-15 20:59:57.421 0.351s",
    "2016-09-15 20:59:58.233 1.181s",
    "2016-09-15 20:59:58.299 0.8s",
    "2016-09-15 20:59:58.688 1.041s",
    "2016-09-15 20:59:59.591 1.412s",
    "2016-09-15 21:00:00.464 1.466s",
    "2016-09-15 21:00:00.741 1.581s",
    "2016-09-15 21:00:00.748 2.31s",
    "2016-09-15 21:00:00.966 0.381s",
    "2016-09-15 21:00:02.066 2.62s"
]))

# answer
# 1
# 2
# 7