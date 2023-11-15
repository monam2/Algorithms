#swea 6808 규영이와 인영이의 카드 게임
# 중복은 x, 순열 아니면 조합
# 조합은 그저 뽑기만 하므로 [(2, 4, 6, 8, 10, 12, 14, 16, 18)]
# 순열은 순서를 고려
#최대 경우의 수는 9! -> 362880. n^2까지는 통과 -> 이중반복 완전탐색
from itertools import permutations

T = int(input())
for t in range(1,T+1):
    #규영이는 card 순서대로 냄.
    inyoung = [i for i in range(1,19)]
    gyuyoung = list(map(int, input().split()))
    for i in gyuyoung:
        inyoung.remove(i)

    gyu_win =0
    in_win = 0
    for i in list(permutations(inyoung, 9)):
        gg = 0
        yy = 0
        for j in range(9):
            gy = gyuyoung[j]
            iy = i[j]
            if gy > iy: #규영이 카드가 인영이보다 높으면 gg에 합을 저장
                gg += gy + iy
            else: #인영이 카드가 규영이보다 높으면 yy에 합을 저장
                yy += gy + iy
        if gg > yy:
            gyu_win += 1
        else:
            in_win += 1

    print(f"#{t} {gyu_win} {in_win}")