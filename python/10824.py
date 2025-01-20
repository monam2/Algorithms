# 10824 네 수

# 입력
# 네 자연수 A,B,C,D
# 출력
# A와 B를 붙인 수 + C와 D를 붙인 수 (합)
# 붙인다? : 20, 30 -> 2030 (문자열로 처리)

arr = list(input().split())
print(int(arr[0]+arr[1]) + int(arr[2]+arr[3]))
