N = int(input())
answer = []
for num in range(1,N+1):
  if num%2 == 0:
    answer.append(num**2)

print(*answer, sep=" ")