# 1439 뒤집기

# 연속되는게 더 많은 거?
# 1이 연속되면 1 추가, 0이 연속되면 0 추가
# 000110 -> 010 -> 이 경우 1을 0으로 바꾸면 1번(최소)
# 100001 -> 101 -> 이 경우 0을 1로 바꾸면 1번(최소)
# 중복없는 수를 담을 배열을 만들고, 앞의 숫자와 다르면 넣는다.
# 그리고 해당 배열에서 0과 1의 갯수를 체크한다. -> 더 적은 것

S = list(input())
noneDup = []

noneDup.append(S[0])

for i in range(1, len(S)):
    if noneDup[-1] == S[i]:
        continue
    noneDup.append(S[i])

zeroCnt = noneDup.count('0')
oneCnt = noneDup.count('1')
if zeroCnt > oneCnt:
    print(oneCnt)
else:
    print(zeroCnt)