# 10101 삼각형 외우기 다른 풀이

triangle = [int(input()) for _ in range(3)]

tri_set = set(triangle)

if sum(triangle) != 180:
    print("Error")
elif len(tri_set) == 1: # 모든 각도가 같음 : 정삼각형
    print('Equilateral')
elif len(tri_set) == 2: # 하나는 같고 하나는 다름 : 이등변 삼각형
    print('Isosceles')
else:
    print('Scalene')