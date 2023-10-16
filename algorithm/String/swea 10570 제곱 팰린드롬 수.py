#SWEA 10570 제곱 팰린드롬 수
import math

T = int(input())
for t in range(T):
    answer = 0
    a,b = map(int, input().split())
    for i in range(a,b+1):
        if i == 1: #1은 무조건 누적
            answer += 1
            continue
        sqrt_n = math.sqrt(i)
        if sqrt_n%1==0.0: #제곱근이 정수라면
            if i<10: #제곱근이 정수일 때 i가 한자리수면 바로 누적
                answer += 1
                continue
            if str(int(sqrt_n)) == str(int(sqrt_n))[::-1]: #회문인지 검사
                if str(i) == str(i)[::-1]:
                    answer += 1

    print(f"#{t+1}", answer)
