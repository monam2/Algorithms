#백준 1940번 주몽

'''
2 7 4 1 5 3
두개의 고유한 번호를 합쳐서 m값을 만들기

목표값 m : 9
오름차순 정렬
1 2 3 4 5 7

투포인터 사용
포인터를 어떻게 이동시킬 것인가?

- left와 right를 더한 값이 m보다 큰 경우
-> right -= 1
- left와 right 더한 값이 m보다 작은 경우
-> left += 1
- left와 right 더한 값이 m이면
-> left += 1
'''
n = int(input())
m = int(input())
arr = list(map(int, input().split()))
arr.sort()

left = 0
right = n-1
count = 0

while left<right:
    sum_p = arr[left] + arr[right]
    if sum_p < m:
        left += 1
    elif sum_p > m:
        right -= 1
    else:
        count += 1
        left += 1
        right -= 1
        
print(count)