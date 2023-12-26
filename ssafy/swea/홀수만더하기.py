#SWEA 홀수만 더하기

#SWEA 최대수 구하기

T = int(input())
for t in range(1,T+1):
    arr = list(map(int, input().split()))
    result = 0
    for num in arr:
        if num==1 or num%2==1:
            result += num
    print(f"#{t} {result}")