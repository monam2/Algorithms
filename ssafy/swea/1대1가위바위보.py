#SWEA 1대1 가위바위보

a, b = map(int, input().split())
if a==3 or b==3:
    if a==2 or b==2:
        answer = 'A' if a>b else 'B'
    else:
        answer = 'A' if a<b else 'B'
else:
    answer = 'A' if a>b else 'B'
print(answer)