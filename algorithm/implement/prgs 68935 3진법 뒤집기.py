#프로그래머스 3진법 뒤집기
def solution(n):
    result = []
    if n<3:
        return n
    else:
        while True:
            div = n//3
            rem = n%3
            n = div
            result.append(rem)
            if n<3:
                break
        result.append(n)
    return int(''.join(map(str, result)),3)

print(solution(45))
