# 1213  팰린드롬 만들기

from collections import Counter

s = input()

# 홀수개인 알파벳이 1개 또는 없어야 함
counts = Counter(s)
hol_cnt = 0
mid_letter = ""
half_letter = ""

for k, v in counts.items():
    if v % 2 == 1:
        hol_cnt += 1
        mid_letter = k

if hol_cnt > 1:
    print("I'm Sorry Hansoo")
else:
    for k, v in sorted(counts.items()):
        half_letter += k * (v // 2)

    result = half_letter + mid_letter + half_letter[::-1]
    print(result)
