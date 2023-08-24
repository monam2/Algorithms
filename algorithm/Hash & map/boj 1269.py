#1269 대칭 차집합
a,b = map(int, input().split())
aa = set(map(int, input().split()))
bb = set(map(int, input().split()))

print(len(aa-bb)+len(bb-aa))
