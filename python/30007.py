# 30007 라면 공식
# W = A(X-1) + B

N = int(input())

for _ in range(N):
    A, B, X = map(int, input().split())

    result = A * (X - 1) + B
    print(result)
