#프로그래머스 12985 예상 대진표

def solution(n,a,b):
    li = [a,b]
    count = 1

    while True:
        new_li = []
        for i in li:
            if i%2 == 0: #짝수
                i = i//2
            else:
                i = i//2+1
            new_li.append(i)
        li = new_li
        
        if li[0] == li[1]:
            return count

        count += 1

print(solution(8,4,7))
