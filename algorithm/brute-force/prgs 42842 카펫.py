#프로그래머스 42842 카펫

def solution(brown, yellow):
    for i in range(1,yellow+1):
        if yellow%i !=0:
            continue
        
        sero = i
        garo = yellow//i

        if ((garo+1) + (sero+1))*2 == brown:
            return [garo+2, sero+2]

print(solution(10,2))
print(solution(8,1))
print(solution(24,24))
