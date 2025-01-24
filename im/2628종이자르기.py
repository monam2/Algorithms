# 2628 종이자르기

# r_list = [0, R]
# c_list = [0, C]
# 이렇게 저장하고, 입력되는 선을 배열에 추가 -> 이후 오름차순 정렬
# 각 list에서 차이를 계산해서 가장 큰 차를 기록(r/c)
# 가장 큰 차 끼리 계산


def calculate(list, gap):
    for i in range(1, len(list)):
        gap = max(gap, list[i] - list[i - 1])

    return gap


R, C = map(int, input().split())
N = int(input())
r_list = [0, R]
c_list = [0, C]

for _ in range(N):
    d, n = map(int, input().split())
    if d == 1:  # 가로
        r_list.append(n)
    elif d == 0:  # 세로
        c_list.append(n)

r_list.sort()
c_list.sort()

r_gap = 0
c_gap = 0

max_r = calculate(r_list, r_gap)
max_c = calculate(c_list, c_gap)

print(max_r * max_c)
