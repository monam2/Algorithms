#백준 1914 하노이 탑
def f(n,a,b,c):
    if n==1:
        print(a, c)
    else: #원반의 위치가 아닌 기둥의 위치를 바꾼다?
        f(n-1, a, c, b) # n-1개를 b 기둥으로 잠깐 옮겨놓기

        f(1, a, b, c) # 가장 밑에 있는 원판을 c 기둥으로 옮기기

        f(n-1, b, a, c) # b 기둥의 나머지 n-1개를 c 기둥으로 옮기기

n = int(input())
print(2**n-1)
if n<=20:
    f(n,1,2,3)