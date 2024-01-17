#백준 4949 균형잡힌 세상


while True:
    stack = []
    str = input()
    if str == ".":
        break
    for s in str:
        if s=='(' or s=='[':
            stack.append(s)
        elif s == ')':
            if len(stack) > 0 and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(')')
                break
        elif s==']':
            if len(stack) > 0 and stack[-1] == '[':
                stack.pop()
            else:
                stack.append(']')
                break
    if len(stack) == 0:
        print('yes')
    else:
        print('no')