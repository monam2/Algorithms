#백준 10866 덱
from collections import deque
import sys
input = sys.stdin.readline

dq = deque()
n = int(input())
for i in range(n):
    ipt = list(input().split())
    if len(ipt) == 1:
        command = ipt[0]
        if command == 'pop_front':
            if dq:
                a = dq.popleft()
                print(a)
            else:
                print(-1)
        elif command == 'pop_back':
            if dq:
                a = dq.pop()
                print(a)
            else:
                print(-1)
        elif command == 'size':
            print(len(dq))
        elif command == 'empty':
            if dq:
                print(0)
            else:
                print(1)
        elif command == 'front':
            if dq:
                print(dq[0])
            else:
                print(-1)
        elif command == 'back':
            if dq:
                print(dq[-1])
            else:
                print(-1)

    else:
        command = ipt[0]
        num = ipt[1]
        if command == 'push_front':
            dq.appendleft(num)
        elif command == 'push_back':
            dq.append(num)