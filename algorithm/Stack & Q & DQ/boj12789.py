#12789
n = int(input())
arr = list(map(int,input().split()))

def a(n, arr):
    stack = []
    idx = 1
    for i in arr:
        stack.append(i)
        while stack and stack[-1]==idx: # 스택 마지막이 1이라면
            stack.pop()
            idx+=1
        if len(stack) > 1 and stack[-1] > stack[-2]:
            return 'Sad'
    if stack:
        return 'Sad'
    else:
        return 'Nice'

print(a(n,arr))
'''
승환이의 앞에 서 있는 학생들의 수와 번호가 주어짐.

왼쪽 대기열 자체가 스택이 되며, 스택으로 넣기 전에 번호가 맞으면 바로 통과시킴.
번호가 안맞으면 스택에 넣음.


반복문을 돌면서 1이 나오면 컨티뉴.
'''
