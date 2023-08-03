'''
시각

00시 00분 00초부터 n시 59분 59초까지 3이 포함되는 수를 체크하는 경우

완전탐색을 이용(brute force)

시, 분, 초 를 각각 반복문으로 구성하여 3중 반복문을 이루면 될듯.

0) 입력 / 
1) for 시간(n)에 대해서 반복
    2) for 분(~59) 까지 반복
        3) for 초(~59) 까지 반복
        문자열로 처리해서 3이 있는지 확인.
'''

n = int(input())
result = 0

for i in range(n+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                result += 1
print(result)
