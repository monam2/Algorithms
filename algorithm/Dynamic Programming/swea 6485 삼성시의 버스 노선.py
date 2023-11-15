#swea 6485 삼성시의 버스 노선

#버스 정류장을 지나는 버스 노선?
# -> 어떤 정류장 C가 Ai~Bi 의 범위에 들어있는가를 체크하면 됨.

T = int(input())
for t in range(1,T+1):
    n = int(input())
    bus = [0]*5001
    for i in range(n):
        a, b = map(int, input().split())
        for j in range(a,b+1):
            bus[j] += 1

    p = int(input())
    result = []
    for i in range(p):
        c = int(input())
        result.append(str(bus[c]))
    print(f"#{t} ", end="")
    for i in result:
        print(i, end=' ')
    print()