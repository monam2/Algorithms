#프로그래머스 JadenCase 문자열 만들기

def solution(s):
    s = s.split(' ')
    arr = []
    for i in s:
        new = i.capitalize()
        arr.append(new)
    return ' '.join(arr)

print(solution("3people unFollowed me"))
print(solution("for the last week"))
