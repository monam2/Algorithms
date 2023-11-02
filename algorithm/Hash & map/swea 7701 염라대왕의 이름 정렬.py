#swea 7701 염라대왕의 이름 정렬

T = int(input())
for t in range(1, T+1):
    name = {}
    n = int(input())
    for i in range(n):
        ipt = input().rstrip()
        if ipt in name:
            name[ipt] += 1
        else:
            name[ipt] = 1
    answer = list(name.keys())
    print(f"#{t}")
    for a in sorted(answer, key=lambda x : (len(x),x)):
        print(a)