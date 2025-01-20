# 1524 세준세비

# 제일 약한 병사가 여러 명이고, 이들이 모두 같은 편에 있다면 임의로 한 명이 죽는다.
# -> 힘이 가장 낮은 애들이 여러명 & 한쪽에 있다면 그들 중 아무나 한명 제거
#
# 제일 약한 병사가 여러명이고, 양편에 모두 있으면 -> 세비(M)의 병사가 죽는다.

T = int(input())

for _ in range(T):
    input()
    N, M = map(int, input().split())
    n_list = list(map(int, input().split()))
    m_list = list(map(int, input().split()))

    n_list.sort(reverse=True)
    m_list.sort(reverse=True)

    while n_list and m_list:
        if n_list[-1] >= m_list[-1]:
            m_list.pop()
        else:
            n_list.pop()

    if n_list:
        print("S")
    elif m_list:
        print("B")
    else:
        print("C")
