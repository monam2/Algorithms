#swea 19003 팰린드롬 문제

def is_pal(s:str):
    return s[::-1]

T = int(input())
for t in range(1,1+T):
    n, m = map(int, input().split())
    arr = []
    pal = []
    for i in range(n):
        s = input()
        if s==s[::-1]:
            pal.append(s)
        else:
            arr.append(s)
    answer = 0
    if len(pal) >= 1:
        answer += m
    leng = len(arr)
    for i in range(leng-1):
        for j in range(i+1, leng):
            if is_pal(arr[i]) == arr[j]:
                answer += 2*m
    print(f"#{t} {answer}")

    #팰린드롬이 아무리 많아도 어짜피 한 개 밖에 못씀 -> answer에 m 누적
    #팰린드롬이 아닌 수 중에서 뒤집으면 같은 문자열 두 개를 찾아서 answer에 m*2 누적
    # -> 이렇게 하는 이유는 aab, baa ,ccb, bcc 가 있으면 결과적으로 팰린드롬이 돼야하므로
    #쌍을 이뤄야함. 쌍을 이룬다는 것은 두 개의 역이 같은지를 확인하는 것