#프로그래머스 42839 소수 찾기
from itertools import permutations
import math
def check(n):
    if n==0 or n==1:
        return False
    for i in range(2,int(math.sqrt(n)+1)):
        if n%i==0:
            return False
    return True

def solution(numbers):
    answer = 0
    arr = []
    before = []
    for i in range(1,len(numbers)+1):
        for a in list(permutations(numbers,i)):
            na = int(''.join(a))
            if na not in before:
                before.append(na)
                if check(na):
                    answer += 1
    return answer
