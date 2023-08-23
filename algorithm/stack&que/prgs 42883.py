#프로그래머스 큰 수 만들기

def solution(number, k):
    stack = []
    for i in number:
        if not stack:
            stack.append(i)
        else:
            while stack and stack[-1] < i and k>0:
                stack.pop()
                k-=1
            stack.append(i)
    if k>0:
        for i in range(k):
            stack.pop()
    return ''.join(stack)


print(solution("4321", 1))
print(solution("1924", 2))
print(solution("1231234", 3))
print(solution("4177252841", 4))
