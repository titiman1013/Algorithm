in_name = [" ", ".", "-"]

def solution(files):
    answer = []

    file_list = []
    for idx, file in enumerate(files):
        file_info = []
        file_idx = 0
        tmp_string = ""
        string_type = 'HEAD'
        while file_idx != len(file):
            if string_type == 'HEAD':
                if file[file_idx].isalpha() or file[file_idx] in in_name:
                    tmp_string += file[file_idx]
                else:
                    file_info.append(tmp_string.lower())
                    string_type = 'NUMBER'
                    tmp_string = file[file_idx]
                    if file_idx + 1 == len(file):
                        file_info.append(int(tmp_string))

            elif string_type == 'NUMBER':
                if file[file_idx].isdecimal():
                    tmp_string += file[file_idx]
                    if file_idx + 1 == len(file):
                        file_info.append(int(tmp_string))
                else:
                    file_info.append(int(tmp_string))
                    break

            file_idx += 1

        file_info.append(idx)
        file_list.append(file_info)

    file_list.sort()

    for head, num, idx in file_list:
        answer.append(files[idx])

    return answer




print(solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]))
print(solution(["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]))
print(solution(["img000012345", "img1.png","img2","IMG02"]))

# answer
# ["img1.png", "IMG01.GIF", "img02.png", "img2.JPG", "img10.png", "img12.png"]
# ["A-10 Thunderbolt II", "B-50 Superfortress", "F-5 Freedom Fighter", "F-14 Tomcat"]