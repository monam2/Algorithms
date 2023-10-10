#SWEA 1974 스도쿠 검증

T = int(input())

for test_case in range(1, T + 1):
    answer = 1
    flag = True
    sdoku = [list(map(int, input().split())) for _ in range(9)]
    
    #가로줄 체크
    
    for arr in sdoku:
        dic = {1:False,2:False,3:False,4:False,5:False,6:False,7:False,8:False,9:False}
        for key,val in dic.items():
            if key in arr:
                dic[key]=True
        if False in dic.values(): #비는 숫자가 있으면 0출력, flag = False
            answer = 0
            flag = False
            break
    #세로줄 체크
    if flag:
        
        for i in range(9):
            dic = {1:False,2:False,3:False,4:False,5:False,6:False,7:False,8:False,9:False}
            for j in range(9):
                dic[sdoku[j][i]] = True
            if False in dic.values(): #비는 숫자가 있으면 0출력, flag = False
                answer = 0
                flag = False
                break
    
    
    #3x3 체크
    if flag:
        for i in range(0,9,3):
            for j in range(0,9,3):
                dic = {1:False,2:False,3:False,4:False,5:False,6:False,7:False,8:False,9:False}
                for m in range(3):
                    for n in range(3):
                        dic[sdoku[i+m][j+n]] = True
                if False in dic.values(): #비는 숫자가 있으면 0출력, flag = False
                    answer = 0
                    flag = False
                    break
    print(f"#{test_case}",answer)
