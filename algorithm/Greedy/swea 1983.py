#swea 1983 조교의 성적 매기기
 
T = int(input())

for test_case in range(1, T + 1):
    result = ['A+','A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
    n, k = map(int, input().split())
    arr = []
    for i in range(n):
        a,b,c = map(int, input().split())
        arr.append(a*0.35+b*0.45+c*0.2)
    find = arr[k-1] #찾는 점수 ex)200점
    arr.sort(reverse=True)
    k_score_idx = arr.index(find)
    answer = k_score_idx//(n//10)
     
    print(f'#{test_case}',result[answer])
