# 10101 삼각형 외우기

# 삼각형의 종류를 구분하기
# 세 각의 크기가 모두 60 : Equilateral -> 정삼각형
# 세 각의 합이 180이고, 두 각이 같은 경우 : Isosceles -> 이등변 삼각형
# 세 각의 합이 180이고, 같은 각이 없는 경우 : Scalene -> 그냥 삼각형
# 세 각의 합이 180이 아닌 경우 : Error -> 삼각형이 아닌 경우

triangle = [int(input()) for _ in range(3)]

if sum(triangle) != 180:
    print('Error')
else:
    triangle.sort()

    if triangle[0] == triangle[1] == triangle[2]:
        print('Equilateral')
    elif triangle[0] == triangle[1] or triangle[1] == triangle[2] or triangle[0] == triangle[2]:
        print('Isosceles')
    else:
        print('Scalene')