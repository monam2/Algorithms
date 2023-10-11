#SWEA 1284 수도 요금 경쟁 (2nd)
#종민놈이 쓰는 물 W리터
#A: 1리터*P원
#B: R리터 이하쓰면 기본 Q원,
#B: R리터보다 많이 쓰면 초과량(사용량-R)*S을 더 냄->기본요금 포함해야함

T = int(input())
for t in range(T):
    p,q,r,s,w = map(int, input().split())
    a = w*p
    if w <= r:
        b = q
    else:
        b = s*(w-r)+q
    print(f"#{t+1}", min(a,b))
