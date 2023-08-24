#프로그래머스 Lv2 이진 변환 반복하기

def solution(s):
    count = 0
    zero = 0
    while s!='1':
        count += 1
        for i in s:
            if i == '0':
                zero += 1 #제거되는 0의 갯수 +1
        s = s.replace('0','')
        dec = len(s)

        result = []
        while dec != 1:
            mo = dec //2
            na = dec % 2
            result.append(na)
            dec = mo
        result.append(dec)
        result.sort(reverse=True)
        result = list(map(str, result))
        s = ''.join(result)

    return [count, zero]


print(solution("110010101001"))
print(solution("01110"))
print(solution("1111111"))
