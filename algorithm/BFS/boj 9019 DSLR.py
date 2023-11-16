# 백준 9019 DSLR
'''
D: D 는 n을 두 배로 바꾼다. 결과 값이 9999 보다 큰 경우에는 10000 으로 나눈 나머지를 취한다. 그 결과 값(2n mod 10000)을 레지스터에 저장한다.
S: S 는 n에서 1 을 뺀 결과 n-1을 레지스터에 저장한다. n이 0 이라면 9999 가 대신 레지스터에 저장된다.
L: L 은 n의 각 자릿수를 왼편으로 회전시켜 그 결과를 레지스터에 저장한다. 이 연산이 끝나면 레지스터에 저장된 네 자릿수는 왼편부터 d2, d3, d4, d1이 된다.
R: R 은 n의 각 자릿수를 오른편으로 회전시켜 그 결과를 레지스터에 저장한다. 이 연산이 끝나면 레지스터에 저장된 네 자릿수는 왼편부터 d4, d1, d2, d3이 된다.
'''
from collections import deque
import sys
input = sys.stdin.readline
def Dd(start):
    new_start = start * 2
    if new_start > 9999:
        new_start %= 10000
    return new_start
def Ss(start):
    new_start = start - 1
    if new_start == -1:
        new_start = 9999
    return new_start
def Ll(start):  # L : 앞에걸 빼서 뒤에 넣음
    new_start = start%1000 + start//1000
    return new_start
def Rr(start):  # R : 뒤에걸 빼서 앞에 넣음
    new_start = start%10//1 + start//10
    return new_start

T = int(input())
for _ in range(T):
    start, end = map(int, input().split())  # 1234 3412

    q = deque()
    q.append((start,""))
    visited = [False]*10000
    visited[start] = True

    while q:
        start, command = q.popleft()
        if start == end:
            print(command)
            break

        #D
        new_start = Dd(start)
        if visited[new_start] == False:
            q.append((new_start, command+'D'))
            visited[new_start] = True
        #S
        new_start = Ss(start)
        if visited[new_start] == False:
            q.append((new_start, command+'S'))
            visited[new_start] = True
        #L
        new_start = Ll(start)
        if visited[new_start] == False:
            q.append((new_start, command+'L'))
            visited[new_start] = True
        #R
        new_start = Rr(start)
        if visited[new_start] == False:
            q.append((new_start, command+'R'))
            visited[new_start] = True



# else:  # L #R
#         newList = []
#         newList.append(start//1000)
#         newList.append(start%1000//100)
#         newList.append(start%1000%100//10)
#         newList.append(start%1000%100%10)

#         new_li = deque(newList)
#         if i == 2:  # L : 앞에걸 빼서 뒤에 넣음
#             tmp = new_li.popleft()
#             new_li.append(tmp)
#         elif i == 3:  # R : 뒤에걸 빼서 앞에 넣음
#             tmp = new_li.pop()
#             new_li.appendleft(tmp)
#         new_start = 1000*new_li[0] + 100*new_li[1] + 10*new_li[2] + new_li[3]