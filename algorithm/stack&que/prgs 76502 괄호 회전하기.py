#프로그래머스 76502 괄호 회전하기
from collections import deque
def solution(s):
    count = 0
    s = deque(s)
    for i in range(len(s)):
        if i != 0:
            p = s.popleft()
            s.append(p)
        stack = []
        right = True
        for j in s:
            if not stack and j in [')', '}', ']']:
                right = False
                break
            elif j in ['(','[','{']:
                stack.append(j)
            elif stack:
                if j == ')' and stack[-1] == '(':
                    stack.pop()
                elif j == ']' and stack[-1] == '[':
                    stack.pop()
                elif j == '}' and stack[-1] == '{':
                    stack.pop()
                    
        if not stack:
            if right == False:
                continue
            else:
                count += 1
    return count
print(solution("[](){}"))
print(solution("}]()[{"))
print(solution("[)(]"))
print(solution("}}}"))
