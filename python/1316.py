# 그룹 단어 체커 1316

# 그룹 단어란?
# -> 문자가 연속하는 경우
# aabbbccb에서 b가 떨어져서 나타나면 그룹단어 아님

N = int(input())

# 현재 글자와 앞의 글자를 비교
# 앞의 글자와 다르면 배열에 저장
# 과정이 끝났을 때, 저장한 배열에 같은 글자가 있으면 탈락

ans = 0
for _ in range(N):
  string = input()
  save = []
  flag = True

  save.append(string[0])
  last = string[0]
  for i in range(1,len(string)):
    if last != string[i]:
      if string[i] in save:
        flag = False
        break
      else:
        save.append(string[i])
        last = string[i]
  
  if flag:
    ans += 1

print(ans)

