# import re

# def solution(new_id):
#     answer = ''

#     new_lst = []
#     spe = ['-', '_']
#     # reg = re.compile(r'[a-z]')
#     for idx, val in enumerate(new_id):
#         # if reg.match(val):
#         if val.upper() != val.lower():
#             new_lst.append(val.lower())
#         elif val.isdigit(): new_lst.append(val)
#         elif val in spe: new_lst.append(val)
#         elif val == '.':
#             if len(new_lst) == 0 or idx == len(new_id) - 1: continue
#             if idx < len(new_id) - 1:
#                 if new_lst[-1] != '.':
#                     new_lst.append(val)
#             else: continue
#     if new_lst:
#         if new_lst[-1] == '.':
#             new_lst.pop()
#     if len(new_lst) == 0:
#         new_lst.append('a')
#     if len(new_lst) >= 16:
#         new_lst = new_lst[:15]
#         if new_lst[-1] == '.':
#             new_lst.pop()
#     elif len(new_lst) <= 2:
#         while len(new_lst) < 3:
#             new_lst.append(new_lst[-1])
#     answer = ''.join(new_lst)

#     return answer



# best solve(정규식)

import re

def solution(new_id):
    st = new_id
    st = st.lower()
    st = re.sub('[^a-z0-9\-_.]', '', st)
    st = re.sub('\.+', '.', st)
    st = re.sub('^[.]|[.]$', '', st)
    st = 'a' if len(st) == 0 else st[:15]
    st = re.sub('^[.]|[.]$', '', st)
    st = st if len(st) > 2 else st + "".join([st[-1] for i in range(3 - len(st))])
    return st





print(solution("...!@BaT#*..y.abcdefghijklm"))
print(solution(	"z-+.^."))
print(solution("=.="))
print(solution("123_.def"))
print(solution("abcdefghijklmn.p"))