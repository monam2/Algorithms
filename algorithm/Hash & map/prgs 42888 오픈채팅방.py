#프로그래머스 오픈채팅방
def solution(record):
    answer = []
    dc = {}

    for i in record:
        a = i.split()
        if a[0] == 'Leave':
            continue
        dc[a[1]] = a[2]

    for i in record:
        b = i.split()
        if b[0] == 'Leave':
            answer.append(f"{dc[b[1]]}님이 나갔습니다.")
        elif b[0] == 'Enter':
            answer.append(f"{dc[b[1]]}님이 들어왔습니다.")
    return answer


# from collections import deque
# def solution(record):
#     answer = []
#     i = 0
#     q = deque()
#     while i<len(record):
#         if record[i].split()[0] == 'Leave':
#             state, id = record[i].split()
#             name = ''
#         else:
#             state, id, name = record[i].split()
        
#         for k in range(len(q)):
#             if q[k][1] == id:
#                 if state == 'Leave':
#                     continue
#                 elif state == 'Change' or state == 'Enter':
#                     q[k][2] = name
#         q.append([state, id, name])
#         i+= 1 #while문 종료

#     for j in q:
#         if j[0] == 'Change':
#             continue
#         elif j[0] == 'Enter':
#             answer.append(f"{j[2]}님이 들어왔습니다.")
#         elif j[0] == 'Leave':
#             answer.append(f"{j[2]}님이 나갔습니다.")
#     return answer

print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))
