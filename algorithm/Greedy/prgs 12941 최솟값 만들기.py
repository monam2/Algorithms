#프로그래머스 12941 최솟값 만들기
def solution(A,B):
    A.sort(reverse = True)
    B.sort()
    
    total = 0
    for i in range(len(A)):
        total += A[i] * B[i]
    return total
