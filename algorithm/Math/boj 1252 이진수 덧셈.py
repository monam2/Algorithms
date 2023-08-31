#1252 이진수 덧셈

a,b = map(str, input().split())
a=int(a, 2)
b=int(b, 2)
print(bin(a+b)[2:])
