#프로그래머스 LV2 숫자의 표현

def solution(n):
    total = 0
    for i in range(1,n+1):
        sum_i =0
        for j in range(i, n+1):
            sum_i += j
            if sum_i == n:
                total+=1
                break
            elif sum_i > n:
                break
    return total
