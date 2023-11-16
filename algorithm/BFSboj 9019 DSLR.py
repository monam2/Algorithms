# 백준 9019 DSLR
'''
D: D 는 n을 두 배로 바꾼다. 결과 값이 9999 보다 큰 경우에는 10000 으로 나눈 나머지를 취한다. 그 결과 값(2n mod 10000)을 레지스터에 저장한다.
S: S 는 n에서 1 을 뺀 결과 n-1을 레지스터에 저장한다. n이 0 이라면 9999 가 대신 레지스터에 저장된다.
L: L 은 n의 각 자릿수를 왼편으로 회전시켜 그 결과를 레지스터에 저장한다. 이 연산이 끝나면 레지스터에 저장된 네 자릿수는 왼편부터 d2, d3, d4, d1이 된다.
R: R 은 n의 각 자릿수를 오른편으로 회전시켜 그 결과를 레지스터에 저장한다. 이 연산이 끝나면 레지스터에 저장된 네 자릿수는 왼편부터 d4, d1, d2, d3이 된다.
'''
from collections import deque

T = int(input())
for t in range(1, 1 + T):
    start, end = map(int, input())  # 1234 3412

    dc = ['D', 'S', 'L', 'R']
    q = deque()
    q.append((start,""))
    visited = {}
    visited[(start, "")] = True
    answer = 0

    while q:
        start, com= q.popleft()
        if start == end:
            answer = com
            break

        if i == 0:  # D
            new_start = start * 2
            if new_start > 9999:
                new_start %= 10000
        elif i == 1:  # S
            new_start = start - 1
            if new_start == 0:
                new_start = 9999
        else:  # L #R
            new_start = list(str(start))
            new_start = deque(new_start)
            if i == 2:  # L : 앞에걸 빼서 뒤에 넣음
                tmp = new_start.popleft()
                new_start.append(tmp)
            elif i == 3:  # R : 뒤에걸 빼서 앞에 넣음
                tmp = new_start.pop()
                new_start.appendleft(tmp)



    for i in range(4):
        command = dc[i]
        new_com = com + command


            new_start = list(new_start)
            new_start = int(''.join(new_start))

        visited[(start), new_com] = True
        q.append((new_com))
