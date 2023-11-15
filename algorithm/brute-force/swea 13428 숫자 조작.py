#swea 13428 숫자 조작

T = int(input())
for t in range(1,T+1):
    n = input()
    if n=='0':
        print(f"#{t} 0 0")
        continue

    #join 사용을 위한 문자열로 병합 후 정수로 변환
    max_value = int(n)
    min_value = int(n)
    # 입력이 10000 이런 경우 어떻게 스왑을 하든 맨앞에 0이 오게됨
    # -> 10000은 최댓값과 최솟값이 같다.

    leng = len(list(n))
    for i in range(leng-1):
        for j in range(i+1, leng):
            new_n = list(n)
            tmp = new_n[i]
            new_n[i] = new_n[j]
            new_n[j] = tmp

            if new_n[0] == '0':
                continue
            chng_n = int(''.join(new_n))
            if chng_n > max_value:
                max_value = chng_n
            if chng_n < min_value:
                min_value = chng_n
    print(f"#{t} {min_value} {max_value}")


# T = int(input())
# for t in range(1,T+1):
#     answer = 0
#     n = list(map(int, list(input())))
#     max_value = 0
#     min_value = 10000000000
#     for i in range(len(n)-1):
#         for j in range(i+1, len(n)):
#             new_n = n
#             tmp = new_n[i]
#             new_n[i] = new_n[j]
#             new_n[j] = tmp
#             if new_n[0] == 0:
#                 continue
#             if int(''.join(list(map(str, new_n)))) > max_value:
#                 max_value = int(''.join(list(map(str, new_n))))
#             if int(''.join(list(map(str, new_n)))) < min_value:
#                 min_value = int(''.join(list(map(str, new_n))))
#     print(f"#{t} {min_value} {max_value}")