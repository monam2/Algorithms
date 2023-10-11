#SWEA 1206 View

# 건물의 길이 항상 1000이하 -> 3중 루프까진 가능
# i-2~i+2를 기준으로 완전탐색
# i에서 i-2, i-1, i+1, i+2를 뺀 값의 최솟값 = 그 건물의 조망 확보 세대수


for test_case in range(1, 11):
    n = int(input())
    answer = 0
    arr = list(map(int, input().split()))
    for i in range(2, n-2):
        if max(arr[i-2], arr[i-1], arr[i], arr[i+1], arr[i+2]) == arr[i]:
            answer += arr[i] - max([arr[i-2], arr[i-1], arr[i+1], arr[i+2]])
    print(f"#{test_case}", answer)
