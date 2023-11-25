#프로그래머스 Lv.2 올바른 괄호

def solution(s):
    arr = list(s)
    stack = []
    i = 0
    while i<len(arr):
        if arr[i] == '(':
            stack.append(1)
        elif not stack and arr[i]==')':
            return False
        elif arr[i] == ')':
            stack.pop()
        i += 1
    if stack:
        return False
    else:
        return True
