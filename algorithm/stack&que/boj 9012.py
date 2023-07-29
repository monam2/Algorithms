#백준 9012

n = int(input())
for _ in range(n):
    arr = list(input())
    stack = []
    i = 0
    result = True
    while i<len(arr):
        if arr[i]=='(':
            stack.append(1)
        elif stack and arr[i] ==')':
            stack.pop()
        elif not stack and arr[i] ==')': #스택이 비어있고, 마지막이 ) 라면
            result = False
            break
        i+= 1

    if stack: #스택에 뭔가가 있으면
        print('NO')
    elif not stack and result == False: #스택이 비어있고, result가 true라면
        print('NO')
    else:
        print('YES')
