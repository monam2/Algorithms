#프로그래머스 Lv2 12980 점프와 순간 이동

def solution(n):
    k = 1
    while n>1:
        if n%2==0:
            n = n//2
        else:
            n -= 1
            k += 1
    return k

print(solution(5))
print(solution(6))
print(solution(5000))
