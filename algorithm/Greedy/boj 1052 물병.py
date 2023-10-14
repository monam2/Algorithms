#백준 1052 물병

n, k = map(int, input().split())

count = 0
answer = -1
while True: #n이랑 bin_n을 함께 가져가기
    if bin(n)[2:].count('1') <= k:
        answer = count
        break
    n += 1
    count += 1

print(answer)
